------------------------------------------------------------------------------
--                                                                          --
--                 GNU ADA RUN-TIME LIBRARY (GNARL) COMPONENTS              --
--                                                                          --
--               S Y S T E M . E X E C U T I V E . T H R E A D S            --
--                                                                          --
--                                  B o d y                                 --
--                                                                          --
--        Copyright (C) 1999-2002 Universidad Politecnica de Madrid         --
--             Copyright (C) 2003-2005 The European Space Agency            --
--                    Copyright (C) 2003-2006, AdaCore                      --
--             Copyright (C) 2003-2001 The European Space Agency            --
--        Copyright (C) 1999-2002 Universidad Politecnica de Madrid         --
--                                                                          --
-- GNARL is free software; you can  redistribute it  and/or modify it under --
-- terms of the  GNU General Public License as published  by the Free Soft- --
-- ware  Foundation;  either version 2,  or (at your option) any later ver- --
-- sion. GNARL is distributed in the hope that it will be useful, but WITH- --
-- OUT ANY WARRANTY;  without even the  implied warranty of MERCHANTABILITY --
-- or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License --
-- for  more details.  You should have  received  a copy of the GNU General --
-- Public License  distributed with GNARL; see file COPYING.  If not, write --
-- to  the Free Software Foundation,  59 Temple Place - Suite 330,  Boston, --
-- MA 02111-1307, USA.                                                      --
--                                                                          --
-- As a special exception,  if other files  instantiate  generics from this --
-- unit, or you link  this unit with other files  to produce an executable, --
-- this  unit  does not  by itself cause  the resulting  executable  to  be --
-- covered  by the  GNU  General  Public  License.  This exception does not --
-- however invalidate  any other reasons why  the executable file  might be --
-- covered by the  GNU Public License.                                      --
--                                                                          --
-- GNARL was developed by the GNARL team at Florida State University.       --
-- Extensive contributions were provided by Ada Core Technologies, Inc.     --
-- The  executive  was developed  by the  Real-Time  Systems  Group  at the --
-- Technical University of Madrid.                                          --
--                                                                          --
------------------------------------------------------------------------------

with System.Parameters;
--  Used for Size_Type

with System.Executive.Parameters;
--  Used for Default_Stack_Size

with System.Executive.Protection;
--  Used for Enter_Kernel
--           Leave_Kernel

with System.Executive.Threads.Queues;
pragma Elaborate (System.Executive.Threads.Queues);
--  Used for Extract_From_Ready
--           Insert_At_Tail
--           Insert_At_Head
--           Change_Priority
--           Running_Thread
--           Environment_Thread_Id

with Unchecked_Conversion;

package body System.Executive.Threads is

   use System.Executive.CPU_Primitives;
   use System.Executive.Time;
   use System.Executive.Parameters;

   use type System.Address;
   use type System.Parameters.Size_Type;

   -----------------
   -- Local data --
   -----------------

   Main_Priority : Integer := -1;
   pragma Import (C, Main_Priority, "__gl_main_priority");

   ---------------------
   -- Local functions --
   ---------------------

   function New_Stack
     (Size : System.Parameters.Size_Type) return System.Address;
   --  Create a new stack of Size bytes. If there is not enough free space
   --  returns System.Null_Address.

   --------------
   -- Get_ATCB --
   --------------

   function Get_ATCB return System.Address is
   begin
      return System.Executive.Threads.Queues.Running_Thread.ATCB;
   end Get_ATCB;

   ------------------
   -- Get_Priority --
   ------------------

   function Get_Priority (Id : Thread_Id) return System.Any_Priority is
   begin
      --  This function does not need to be protected by Enter_Kernel and
      --  Leave_Kernel, because the Active_Priority value is only updated
      --  by Set_Priority (atomically). Moreover, Active_Priority is
      --  marked as Volatile.

      return Id.Active_Priority;
   end Get_Priority;

   ----------------
   -- Initialize --
   ----------------

   procedure Initialize is
      Base_Priority : System.Any_Priority;

   begin
      Protection.Enter_Kernel;

      --  If priority is not specified then the default priority will be used

      if Main_Priority not in System.Any_Priority then
         Base_Priority := System.Default_Priority;
      else
         Base_Priority := Main_Priority;
      end if;

      --  The environment thread is created. This thread executes the
      --  main procedure of the program.

      --  The active priority is initially equal to the base priority

      Queues.Environment_Thread_Id.Base_Priority   := Base_Priority;
      Queues.Environment_Thread_Id.Active_Priority := Base_Priority;

      --  Insert environment thread into the ready queue

      Queues.Insert_At_Head (Queues.Environment_Thread_Id);

      --  The currently executing thread is the environment thread

      Queues.Running_Thread := Queues.Environment_Thread_Id;

      --  Store stack information

      Queues.Environment_Thread_Id.Top_Of_Stack := Top_Of_Environment_Stack;
      Queues.Environment_Thread_Id.Stack_Size   := Environment_Stack_Size;

      --  Initialize the saved registers, including the program
      --  counter and the stack pointer for the environment
      --  thread. The stack for the environment thread must be created
      --  first.

      Initialize_Context
        (Queues.Environment_Thread_Id.Context'Access,
         System.Null_Address,
         System.Null_Address,
         Base_Priority,
         Top_Of_Environment_Stack);

      --  Initialize alarm status

      Queues.Environment_Thread_Id.Alarm_Time :=
        System.Executive.Time.Time'Last;
      Queues.Environment_Thread_Id.Next_Alarm := Null_Thread_Id;

      Protection.Leave_Kernel;
   end Initialize;

   ---------------
   -- New_Stack --
   ---------------

   type Stack_Element is new Natural;
   for Stack_Element'Size use 64;
   --  The elements in the stack must be 64 bits wide to allow double
   --  word data movements.

   subtype Range_Of_Stack is System.Parameters.Size_Type range
     1 .. (System.Executive.Parameters.Stack_Area_Size /
             (Stack_Element'Size / 8) + 1);
   type Stack_Space is array (Range_Of_Stack) of Stack_Element;
   --  The total space for stacks is equal to the Stack_Area_Size
   --  defined in System.Executive.Parameters (in bytes), rounded
   --  to the upper 8 bytes bound.

   Stack : Stack_Space;
   for Stack'Alignment use Standard'Maximum_Alignment;
   --  Object to store all the stacks. It represents the stack
   --  space. The stack must be aligned to the maximum.

   Index : Range_Of_Stack := Range_Of_Stack'Last;
   --  Index points to the top of the free stack space

   function New_Stack
     (Size : System.Parameters.Size_Type) return System.Address
   is
      Real_Size : constant System.Parameters.Size_Type :=
                    (Size / (Stack_Element'Size / 8)) + 1;
      --  Translate Size into bytes to eight bytes size

      Old_Index : Range_Of_Stack;

   begin
      --  If we try to allocate more stack than available System.Null_Address
      --  is returned. Otherwise return address of the top of the stack.

      if (Index - Range_Of_Stack'First) < Real_Size then
         return System.Null_Address;
      else
         Old_Index := Index;
         Index := Index - Real_Size;
         return Stack (Old_Index)'Address;
      end if;
   end New_Stack;

   --------------
   -- Set_ATCB --
   --------------

   procedure Set_ATCB (ATCB : System.Address) is
   begin
      --  Set_ATCB is only called in the initialization of the task, and
      --  just by the owner of the thread, so there is no need of explicit
      --  kernel protection when calling this function.

      System.Executive.Threads.Queues.Running_Thread.ATCB := ATCB;
   end Set_ATCB;

   ------------------
   -- Set_Priority --
   ------------------

   procedure Set_Priority (Priority  : System.Any_Priority) is
   begin
      Protection.Enter_Kernel;

      --  The Ravenscar profile does not allow dynamic priority changes. Tasks
      --  change their priority only when they inherit the ceiling priority of
      --  a PO (Ceiling Locking policy). Hence, the task must be running when
      --  changing the priority. It is not possible to change the priority of
      --  another thread within the Ravenscar profile, so that is why
      --  Running_Thread is used.

      --  Priority changes are only possible as a result of inheriting
      --  the ceiling priority of a protected object. Hence, it can
      --  never be set a priority which is lower than the base
      --  priority of the thread.

      pragma Assert (Priority >= Queues.Running_Thread.Base_Priority);

      Queues.Change_Priority (Queues.Running_Thread, Priority);

      Protection.Leave_Kernel;
   end Set_Priority;

   -----------
   -- Sleep --
   -----------

   procedure Sleep is
   begin
      Protection.Enter_Kernel;

      Queues.Extract_From_Ready (Queues.Running_Thread);

      --  The currently executing thread is now blocked, and it will leave
      --  the CPU when executing the Leave_Kernel procedure.

      Protection.Leave_Kernel;

      --  Now the thread has been awaken again and it is executing
   end Sleep;

   -------------------
   -- Thread_Create --
   -------------------

   procedure Thread_Create
     (Id         : out Thread_Id;
      Code       : System.Address;
      Arg        : System.Address;
      Priority   : System.Any_Priority;
      Stack_Size : System.Parameters.Size_Type)
   is
      Stack_Address : System.Address;

   begin
      Protection.Enter_Kernel;

      --  Create the stack

      Stack_Address := New_Stack (Stack_Size);

      if Stack_Address = System.Null_Address then

         --  If there is not enough stack then the thread cannot be created.
         --  Return an invalid identifier for signaling the problem.

         Id := Null_Thread_Id;

      else
         --  The first free position is assigned to the new thread

         Id := Queues.New_Thread_Descriptor;

         --  If the maximum number of threads supported by the kernel has been
         --  exceeded, a Null_Thread_Id is returned.

         if Id /= Null_Thread_Id then

            --  Set the base and active priority

            Id.Base_Priority   := Priority;
            Id.Active_Priority := Priority;

            --  Insert task inside the ready list (as last within its priority)

            Queues.Insert_At_Tail (Id);

            --  Store stack information

            Id.Top_Of_Stack := Stack_Address;
            Id.Stack_Size   := Stack_Size;

            --  Initialize the saved registers, including the program
            --  counter and stack pointer. The thread will execute the
            --  Thread_Caller procedure and the stack pointer points to
            --  the top of the stack assigned to the thread.

            Initialize_Context
              (Id.Context'Access,
               Code,
               Arg,
               Priority,
               Stack_Address);

            --  Initialize alarm status

            Id.Alarm_Time := System.Executive.Time.Time'Last;
            Id.Next_Alarm := Null_Thread_Id;
         end if;
      end if;

      Protection.Leave_Kernel;
   end Thread_Create;

   -----------------
   -- Thread_Self --
   -----------------

   function Thread_Self return Thread_Id is
   begin
      --  Return the thread that is currently executing

      return Queues.Running_Thread;
   end Thread_Self;

   ------------
   -- Wakeup --
   ------------

   procedure Wakeup (Id : Thread_Id) is
   begin
      Protection.Enter_Kernel;

      --  Insert the thread at the tail of its active priority so that the
      --  thread will resume execution.

      System.Executive.Threads.Queues.Insert_At_Tail (Id);

      Protection.Leave_Kernel;
   end Wakeup;

   -----------
   -- Yield --
   -----------

   procedure Yield is
   begin
      Protection.Enter_Kernel;

      --  Move the currently running thread to the tail of its active priority

      Queues.Extract_From_Ready (Queues.Running_Thread);
      Queues.Insert_At_Tail (Queues.Running_Thread);

      Protection.Leave_Kernel;
   end Yield;

end System.Executive.Threads;
