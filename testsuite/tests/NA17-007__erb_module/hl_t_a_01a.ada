------------------------------------------------------------------------------
--                                                                          --
--                          ESA RAVENSCAR BENCHMARK                         --
--                                                                          --
--                         H L _ T _ A _ 0 1 . A D A                        --
--                                                                          --
--                                 B o d y                                  --
--                                                                          --
--               Copyright (C) 2006, The European Space Agency              --
--                                                                          --
-- The ESA  Ravenscar Benchmark is free  software;  you can  redistribute   --
-- it and/or modify it under  terms of the  GNU General Public License as   --
-- published  by the  Free  Software  Foundation;  either  version 2,  or   --
-- (at your option)  any  later  version.  This benchmark is  distributed   --
-- in the hope that it will be useful, but WITHOUT ANY WARRANTY;  without   --
-- even  the  implied  warranty  of  MERCHANTABILITY  or  FITNESS  FOR  A   --
-- PARTICULAR  PURPOSE.   See the  GNU General  Public License  for  more   --
-- details.  You should have  received  a copy of the GNU General  Public   --
-- License  distributed with GNAT;  see file  COPYING.  If not, write  to   --
-- the Free Software Foundation, 59 Temple Place - Suite 330, Boston,  MA   --
-- 02111-1307, USA.                                                         --
--                                                                          --
-- This benchmark was originally developed by ACT Europe and the Technical  --
-- University  of  Madrid (UPM) under  a contract funded  by  the European  --
-- Space (Statement of Work ref. TOS-EME/02-85/MRN)                         --
--                                                                          --
------------------------------------------------------------------------------

--  Dhrystone
--  For: Ravenscar
--  Measurement: Timing
--  Based on: ACES cl_dh02

with Support_Timing;       use Support_Timing;
with Support_Types; use Support_Types;

package hl_t_a_01a_Global_Def is

   --  Global type definitions

   type Enumeration is (Ident_1, Ident_2, Ident_3, Ident_4, Ident_5);

   subtype One_To_Thirty is Support_Types.Integer16 range 1 .. 30;
   subtype One_To_Fifty is Support_Types.Integer16 range 1 .. 50;
   subtype Capital_Letter is Character range 'A' .. 'Z';

   type String_30 is array (One_To_Thirty) of Character;
   pragma Pack (String_30);

   type Array_1_Dim_Integer is array (One_To_Fifty) of Support_Types.Integer16;
   type Array_2_Dim_Integer is array (One_To_Fifty, One_To_Fifty)
     of Support_Types.Integer16;

   type Record_Type (Discr : Enumeration := Ident_1);

   type Record_Pointer is access all Record_Type;

   type Record_Type (Discr : Enumeration := Ident_1) is record
      Pointer_Comp : Record_Pointer;
      case Discr is
         when Ident_1 =>
            --  Only this variant is used,
            --  but in some cases discriminant
            --  checks are necessary
            Enum_Comp                : Enumeration;
            Int_Comp                 : One_To_Fifty;
            String_Comp              : String_30;
         when Ident_2 =>
            Enum_Comp_2              : Enumeration;
            String_Comp_2            : String_30;
         when others =>
            Char_Comp_1, Char_Comp_2 : Character;
      end case;
   end record;

end hl_t_a_01a_Global_Def;


with Support_Timing;       use Support_Timing;
with Support_Types; use Support_Types;
with hl_t_a_01a_Global_Def; use  hl_t_a_01a_Global_Def;

pragma Elaborate(hl_t_a_01a_Global_Def);

package hl_t_a_01a_Support is

   procedure Proc_0;
   procedure Proc_1 (Pointer_Par_In : in Record_Pointer);
   procedure Proc_2 (Int_Par_In_Out : in out One_To_Fifty);
   procedure Proc_3 (Pointer_Par_Out : out Record_Pointer);

   Int_Glob    : Support_Types.Integer16;
   Char_Glob_1 : Character;

end hl_t_a_01a_Support;

with Support_Timing;       use Support_Timing;
with Support_Types; use Support_Types;
with hl_t_a_01a_Global_Def; use  hl_t_a_01a_Global_Def;

pragma Elaborate(hl_t_a_01a_Global_Def);

package D2_Pack_2 is

   procedure Proc_6 (Enum_Par_In  : in Enumeration;
                     Enum_Par_Out : out Enumeration);
   procedure Proc_7 (Int_Par_In_1, Int_Par_In_2 : in One_To_Fifty;
                     Int_Par_Out                : out One_To_Fifty);
   procedure Proc_8 (Array_Par_In_Out_1         : in out Array_1_Dim_Integer;
                     Array_Par_In_Out_2         : in out Array_2_Dim_Integer;
                     Int_Par_In_1, Int_Par_In_2 : in Support_Types.Integer16);
   function Func_1 (Char_Par_In_1, Char_Par_In_2 : in Capital_Letter)
                   return Enumeration;
   function Func_2 (String_Par_In_1, String_Par_In_2 : in String_30)
                   return Boolean;
end D2_Pack_2;

with hl_t_a_01a_Global_Def, hl_t_a_01a_Support;
use  hl_t_a_01a_Global_Def;

pragma Elaborate(hl_t_a_01a_Support, hl_t_a_01a_Global_Def);

procedure hl_t_a_01a is

   pragma Suppress(Access_Check);
   pragma Suppress(Discriminant_Check);
   pragma Suppress(Index_Check);
   pragma Suppress(Length_Check);
   pragma Suppress(Range_Check);
   pragma Suppress(Division_Check);
   pragma Suppress(Overflow_Check);
   pragma Suppress(Elaboration_Check);
   pragma Suppress(Storage_Check);

begin
   hl_t_a_01a_Support.Proc_0;
end hl_t_a_01a;

with hl_t_a_01a_Global_Def; use  hl_t_a_01a_Global_Def;
with D2_Pack_2;
with Support_Types; use  Support_Types;

pragma Elaborate (hl_t_a_01a_Global_Def);

package body hl_t_a_01a_Support is

   pragma Suppress(Access_Check);
   pragma Suppress(Discriminant_Check);
   pragma Suppress(Index_Check);
   pragma Suppress(Length_Check);
   pragma Suppress(Range_Check);
   pragma Suppress(Division_Check);
   pragma Suppress(Overflow_Check);
   pragma Suppress(Elaboration_Check);
   pragma Suppress(Storage_Check);

   Bool_Glob    : Boolean;
   Char_Glob_2  : Character;
   Array_Glob_1 : Array_1_Dim_Integer;
   Array_Glob_2 : Array_2_Dim_Integer;

   Glob      : aliased Record_Type;
   Glob_Next : aliased Record_Type;

   Pointer_Glob : Record_Pointer;
   Pointer_Glob_Next : Record_Pointer;

   procedure Proc_4;
   procedure Proc_5;

   procedure Proc_0 is
      Int_Loc_1, Int_Loc_2, Int_Loc_3 : One_To_Fifty;
      Char_Loc                        : Character;
      --  This variable is never referenced, it has
      --  not been removed because it occurs in a
      --  "STANDARD" program.
      Enum_Loc                        : Enumeration;
      String_Loc_1, String_Loc_2      : String_30;

      --  variables for rate calculation added in Version 2.1
      Number_Of_Runs                  : Support_Types.Integer16 :=
        Support_Types.Integer16 (Support_Types.Float_5 * 1_000.0);
      --  value of 1000
      Packing_Not_Effective           : exception;
   begin
      --  Initializations

      --  Use default definition:
      hl_t_a_01a_Support.Pointer_Glob_Next := Glob_Next'Access;
      hl_t_a_01a_Support.Pointer_Glob := Glob'Access;
      hl_t_a_01a_Support.Pointer_Glob.all :=
        (Pointer_Comp => hl_t_a_01a_Support.Pointer_Glob_Next,
         Discr        => Ident_1,
         Enum_Comp    => Ident_3,
         Int_Comp     => 40,
         String_Comp  => "DHRYSTONE PROGRAM, SOME STRING");
      String_Loc_1 := "DHRYSTONE PROGRAM, 1'ST STRING";


      begin
         --  tcl 23 April 1992, PCR #91 added code to verify that
         --         packing is effective. The test problem assumes
         --         a target processor with a STORAGE_UNIT based on
         --         an 8-bit byte and that packing to the bit is
         --         effective for boolean_arrays.
         --
         --         This test is for "medium packing" and does not
         --         require a system to allocate an addressable object
         --         (a character) which spans a storage_unit boundary.
         --         The test will fail when the compilation system
         --         could allocate several characters within one
         --         one storage_unit but does not. The expression
         --               ( x - (s-1) / x )
         --         will yield the integral number of times "s" units
         --         will fit within "x."

         if  hl_t_a_01a_Global_Def.String_30'Size >
           30 * Support_Types.System_Storage_Unit  /
           ((Character'Size + Support_Types.System_Storage_Unit - 1) /
            Character'Size)
         then
            raise Packing_Not_Effective;
         end if;

         --  <init_variables>
 --  <start_comment>
 --  Dhrystone Version 2.1 without suppression.
 --  <end_comment>
         --  <start_measure>

         --  In ACEC version 1, array_glob_2(8,7) was set to zero here.
         --  Dhrystone Version 2.1 sets it to 10 outside "Dhrystone
         --  timing loop".  It must be reset each time the ACES timing
         --  loop is executed, or it can provoke an integer overflow
         --  (it is incremented each time PROC_8 is called). There may
         --  be a discrepancy with other sources of Dhrystone here.

         --  Initialize the element which gets incremented
         --  repetitively within program added in version 2.1:
         Array_Glob_2 (8, 7) := 10;
         for Run_Index in 1 .. Number_Of_Runs loop
            Proc_5;
            Proc_4;
            --  Char_Glob_1 = 'A', Char_Glob_2 = 'B', Bool_Glob = False
            Int_Loc_1 := 2;
            Int_Loc_2 := 3;
            String_Loc_2 := "DHRYSTONE PROGRAM, 2'ND STRING";
            Enum_Loc := Ident_2;
            Bool_Glob := not D2_Pack_2.Func_2 (String_Loc_1, String_Loc_2);
            --  Bool_Glob = true
            while Int_Loc_1 < Int_Loc_2 loop
               --  loop body executed once
               Int_Loc_3 := 5 * Int_Loc_1 - Int_Loc_2;
               --  Int_Loc_3 = 7
               D2_Pack_2.Proc_7 (Int_Loc_1, Int_Loc_2, Int_Loc_3);
               --  Int_Loc_3 = 7
               Int_Loc_1 := Int_Loc_1 + 1;
            end loop;
            -- Int_Loc_1 = 3
            D2_Pack_2.Proc_8 (Array_Glob_1,
                              Array_Glob_2,
                              Int_Loc_1,
                              Int_Loc_3);
            -- Int_Glob = 5
            Proc_1 (Pointer_Glob);
            for Char_Index in 'A' .. Char_Glob_2 loop
               -- Loop body executed twice:
               if Enum_Loc = D2_Pack_2.Func_1 (Char_Index, 'C') then
                  --  Not executed d2_pack_2.proc_6 (Ident_1, Enum_Loc);
                  D2_Pack_2.Proc_6(Ident_1, Enum_Loc);
                  String_Loc_2 := "DHRYSTONE PROGRAM, 3'RD STRING";
                  Int_Loc_2 := Run_Index;
                  Int_Glob := Run_Index;
               end if;
            end loop;
            Int_Loc_2 := Int_Loc_2 * Int_Loc_1;
            Int_Loc_1 := Int_Loc_2 / Int_Loc_3;
            Int_Loc_2 := 7 * (Int_Loc_2 - Int_Loc_3) - Int_Loc_1;
            Proc_2 (Int_Loc_1);
         end loop;

         --  <end_measure>

         if Int_Glob /= 5 then
            raise Packing_Not_Effective;
            --  Wrong value for int_glob: should be 5
         end if;

         if Bool_Glob /= True then
            --  Wrong value for bool_glob: should be true; is false
            raise Packing_Not_Effective;
         end if;

         if Char_Glob_1 /= 'A' then
            --  Wrong value for char_glob: should be 'A'; is
            raise Packing_Not_Effective;
         end if;

         if Char_Glob_2 /= 'B' then
            raise Packing_Not_Effective;
            --  Wrong value for char_glob_2: should be 'B'
         end if;

         if Array_Glob_1(8) /= 7 then
            --  Wrong value for array_glob_1(8): should be 7
            raise Packing_Not_Effective;
         end if;

         if Array_Glob_2(8, 7) /= Number_Of_Runs + 10 then
            -- Wrong value for array_glob_2(8,7)
            raise Packing_Not_Effective;
         end if;


         if Pointer_Glob.Discr /= Ident_1 then
            --  Wrong value for pointer_glob.discr: should be IDENT_1
            raise Packing_Not_Effective;
         end if;

         if Pointer_Glob.Enum_Comp /= Ident_3 then
            --  Wrong value for pointer_glob.enum_comp: should be IDENT_3
            raise Packing_Not_Effective;
         end if;

         if Pointer_Glob.Int_Comp /= 17 then
            --  Wrong value for pointer_glob.int_comp: should be 17
            raise Packing_Not_Effective;
         end if;

         if Pointer_Glob.String_Comp /= "DHRYSTONE PROGRAM, SOME STRING" then
            --  Wrong value for pointer_glob.string_comp: should be
            raise Packing_Not_Effective;
         end if;


         if Pointer_Glob_Next.Discr /= Ident_1 then
            --  Wrong value for pointer_glob_next.discr: should be IDENT_1
            raise Packing_Not_Effective;
         end if;

         if Pointer_Glob_Next.Enum_Comp /= Ident_2 then
            --  Wrong value for pointer_glob_next.enum_comp: should be IDENT_2
            raise Packing_Not_Effective;
         end if;

         if Pointer_Glob_Next.Int_Comp /= 18 then
            --  Wrong value for pointer_glob_next.int_comp: should be 18
            raise Packing_Not_Effective;
         end if;

         if Pointer_Glob_Next.String_Comp /= "DHRYSTONE PROGRAM, SOME STRING"
         then
            --  Wrong value for pointer_glob_next.string_comp
            --  Should be  "DHRYSTONE PROGRAM, SOME STRING"
            raise Packing_Not_Effective;
         end if;

         if Int_Loc_1 /= 5 then
            --  Wrong value for int_loc_1: should be 5
            raise Packing_Not_Effective;
         end if;

         if Int_Loc_2 /= 13 then
            --  Wrong value for int_loc_2: should be 13
            raise Packing_Not_Effective;
         end if;

         if Int_Loc_3 /= 7 then
            --  Wrong value for int_loc_3: should be 7
            raise Packing_Not_Effective;
         end if;

         if Enum_Loc /= Ident_2 then
            --  Wrong value for enum_loc: should be ident_2
            raise Packing_Not_Effective;
         end if;

         if String_Loc_1 /= "DHRYSTONE PROGRAM, 1'ST STRING" then
            --  Wrong value for string_loc_1:
            --  should be "DHRYSTONE PROGRAM, 1'ST STRING"
            raise Packing_Not_Effective;
         end if;

         if String_Loc_2 /= "DHRYSTONE PROGRAM, 2'ND STRING" then
            --  Wrong value for string_loc_1:
            --  should be "DHRYSTONE PROGRAM, 2'ND STRING"
            raise Packing_Not_Effective;
         end if;
      end;
   end Proc_0;

   procedure Proc_1 (Pointer_Par_In : in Record_Pointer) is
      Next_Record : Record_Type renames
        Pointer_Par_In.Pointer_Comp.all;
   begin
      Next_Record := Pointer_Glob.all;
      Pointer_Par_In.Int_Comp := 5;
      Next_Record.Int_Comp := Pointer_Par_In.Int_Comp;
      Next_Record.Pointer_Comp := Pointer_Par_In.Pointer_Comp;
      Proc_3 (Next_Record.Pointer_Comp);
      if Next_Record.Discr = Ident_1 then
         Next_Record.Int_Comp := 6;
         D2_Pack_2.Proc_6 (Pointer_Par_In.Enum_Comp, Next_Record.Enum_Comp);
         Next_Record.Pointer_Comp := Pointer_Glob.Pointer_Comp;
         D2_Pack_2.Proc_7 (Next_Record.Int_Comp, 10, Next_Record.Int_Comp);
      else
         Pointer_Par_In.all := Next_Record;
      end if;
   end Proc_1;

   procedure Proc_2 (Int_Par_In_Out : in out One_To_Fifty) is
      Int_Loc  : One_To_Fifty;
      Enum_Loc : Enumeration;
   begin
      Int_Loc := Int_Par_In_Out + 10;
      loop
         if Char_Glob_1 = 'A' then
            Int_Loc := Int_Loc - 1;
            Int_Par_In_Out := Int_Loc - Int_Glob;
            Enum_Loc := Ident_1;
         end if;

         exit when Enum_Loc = Ident_1;
      end loop;
   end Proc_2;

   procedure Proc_3 (Pointer_Par_Out : out Record_Pointer) is
   begin
      if Pointer_Glob /= null then
         Pointer_Par_Out := Pointer_Glob.Pointer_Comp;
      end if;

      D2_Pack_2.Proc_7 (10, Int_Glob, Pointer_Glob.Int_Comp);
   end Proc_3;

   procedure Proc_4 is
      Bool_Loc : Boolean;
   begin
      Bool_Loc := Char_Glob_1 = 'A';
      Bool_Glob := Bool_Loc or Bool_Glob;
      Char_Glob_2 := 'B';
   end Proc_4;

   procedure Proc_5 is
   begin
      Char_Glob_1 := 'A';
      Bool_Glob := False;
   end Proc_5;

end hl_t_a_01a_Support;

with hl_t_a_01a_Global_Def, hl_t_a_01a_Support;
use  hl_t_a_01a_Global_Def;

pragma Elaborate (hl_t_a_01a_Support, hl_t_a_01a_Global_Def);
package body D2_Pack_2 is

   pragma Suppress (Access_Check);
   pragma Suppress (Discriminant_Check);
   pragma Suppress (Index_Check);
   pragma Suppress (Length_Check);
   pragma Suppress (Range_Check);
   pragma Suppress (Division_Check);
   pragma Suppress (Overflow_Check);
   pragma Suppress (Elaboration_Check);
   pragma Suppress (Storage_Check);

   function Func_3 (Enum_Par_In : in Enumeration) return Boolean;

   procedure Proc_6
     (Enum_Par_In  : Enumeration;
      Enum_Par_Out : out Enumeration)
   is
   begin
      Enum_Par_Out := Enum_Par_In;
      if not Func_3 (Enum_Par_In) then
         Enum_Par_Out := Ident_4;
      end if;
      case Enum_Par_In is
         when Ident_1 =>
            Enum_Par_Out := Ident_1;
         when Ident_2 =>
            if hl_t_a_01a_Support.Int_Glob > 100 then
               Enum_Par_Out := Ident_1;
            else
               Enum_Par_Out := Ident_4;
            end if;
         when Ident_3 =>
            Enum_Par_Out := Ident_2;
         when Ident_4 =>
            null;
         when Ident_5 =>
            Enum_Par_Out := Ident_3;
      end case;
   end Proc_6;

   procedure Proc_7
     (Int_Par_In_1, Int_Par_In_2 : One_To_Fifty;
      Int_Par_Out                : out One_To_Fifty)
   is
      Int_Loc : One_To_Fifty;
   begin
      Int_Loc := Int_Par_In_1 + 2;
      Int_Par_Out := Int_Par_In_2 + Int_Loc;
   end Proc_7;

   procedure Proc_8
     (Array_Par_In_Out_1         : in out Array_1_Dim_Integer;
      Array_Par_In_Out_2         : in out Array_2_Dim_Integer;
      Int_Par_In_1, Int_Par_In_2 : in Support_Types.Integer16)
   is
      Int_Loc : One_To_Fifty;
   begin
      Int_Loc := Int_Par_In_1 + 5;
      Array_Par_In_Out_1 (Int_Loc) := Int_Par_In_2;
      Array_Par_In_Out_1 (Int_Loc + 1) := Array_Par_In_Out_1 (Int_Loc);
      Array_Par_In_Out_1 (Int_Loc + 30) := Int_Loc;
      for Int_Index in Int_Loc .. Int_Loc + 1 loop
         Array_Par_In_Out_2 (Int_Loc, Int_Index) := Int_Loc;
      end loop;
      Array_Par_In_Out_2 (Int_Loc, Int_Loc - 1) :=
        Array_Par_In_Out_2 (Int_Loc, Int_Loc - 1) + 1;
      Array_Par_In_Out_2 (Int_Loc + 20, Int_Loc) :=
        Array_Par_In_Out_1 (Int_Loc);
      hl_t_a_01a_Support.Int_Glob := 5;
   end Proc_8;


   function Func_1
     (Char_Par_In_1 : Capital_Letter;
      Char_Par_In_2 : Capital_Letter)
     return Enumeration is
      Char_Loc_1, Char_Loc_2 : Capital_Letter;
   begin
      Char_Loc_1 := Char_Par_In_1;
      Char_Loc_2 := Char_Loc_1;
      if Char_Loc_2 /= Char_Par_In_2 then
         return Ident_1;
      else
         hl_t_a_01a_Support.Char_Glob_1 := Char_Loc_1;
         return Ident_2;
      end if;
   end Func_1;

   function Func_2
     (String_Par_In_1 : String_30;
      String_Par_In_2 : in String_30)
     return Boolean
   is
      Int_Loc  : One_To_Thirty;
      Char_Loc : Capital_Letter;
   begin
      Int_Loc := 2;
      while Int_Loc <= 2 loop
         if Func_1 (String_Par_In_1 (Int_Loc),
                   String_Par_In_2 (Int_Loc + 1)) = Ident_1 then
            Char_Loc := 'A';
            Int_Loc := Int_Loc + 1;
         end if;
      end loop;
      if Char_Loc >= 'W' and Char_Loc < 'Z' then
         Int_Loc := 7;
      end if;
      if Char_Loc = 'R' then
         return True;
      else
         if String_Par_In_1 = String_Par_In_2 then
            Int_Loc := Int_Loc + 7;
            hl_t_a_01a_Support.Int_Glob := Int_Loc;
            return True;
         else
            return False;
         end if;
      end if;
   end Func_2;

   function Func_3 (Enum_Par_In : Enumeration) return Boolean is
      Enum_Loc : Enumeration;
   begin
      Enum_Loc := Enum_Par_In;
      if Enum_Loc = Ident_3 then
         return True;
      else
         return False;
      end if;
   end Func_3;

end D2_Pack_2;
