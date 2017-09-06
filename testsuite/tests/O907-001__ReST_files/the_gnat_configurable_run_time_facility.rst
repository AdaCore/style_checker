.. _The_GNAT_Configurable_Run_Time_Facility:

***************************************
The GNAT Configurable Run Time Facility
***************************************

.. index:: Configurable run-time

This chapter describes how to configure the GNAT run-time library,
based on specific application requirements.

.. _Standard_Run-Time_Mode:

Standard Run-Time Mode
======================

In normal mode, the run-time library supplied by GNAT Pro is complete and
provides all features specified in the Ada Reference Manual.
As far as is practical, only
those sections of the run time that are actually needed are linked,
so the entire run time library is not always included.
Nevertheless, some minimal
required set of run-time units is always linked, and therefore the minimal
run-time library in this normal mode contains a significant amount of code
that may not be required in all operating configurations.

In this standard mode, the run-time library is required to be complete.
If the compiler detects that the run-time library lacks interfaces for
required language features, then the run-time library is considered to
be improperly configured or installed, and a fatal error message is given.

.. _The_Configurable_Run_Time:

The Configurable Run Time
=========================

The Configurable Run Time capability allows the creation of run-time
configurations that support only a subset of the full Ada language.
There are several reasons for providing this kind of subsetting:

  .. index:: Bare-board configuration

* In bare-board situations,
  it may be desirable to minimize the amount of
  run-time code by removing features that are not required.
  As noted above,
  this happens to some extent with the standard run-time library, because
  on most operating systems the linker will
  link in only those units that are referenced by a given program. However,
  the configurable option allows much finer control, and much smaller amounts
  of run-time code end up included in an image.

* When using GNAT Pro in High-Integrity mode, you need to restrict the run-time
  to units that are certifiable.
  Since the certification process may require significant resources,
  it is often desirable to reduce this certification effort by minimizing
  the run-time.

* It may be desirable for stylistic reasons to restrict the language subset
  that is used (e.g., to eliminate tasking). This may for example be useful
  in the case where an application is to be certified, since some features
  make certification much more difficult. This subsetting can be achieved
  to some extent using the pragma ``Restrictions`` mechanism defined
  in the :title:`Ada Reference Manual`. The configurable GNAT run-time facility
  augments this capability by providing much finer grained support.

* When a given set of restrictions is enforced for a program, it may be
  possible to simplify the corresponding run-time library.
  This is done in certain
  cases when pragma ``Restrictions`` is specified in full run-time mode, but
  given the large set of restrictions that can be specified, it is
  not possible to do this tailoring automatically.

.. index:: Zero Footprint Profile

Using the configurable run-time capability, you
can choose any level of support from the full run-time library to a minimal
*Zero Footprint* Profile
which generates no run-time code at all.
The units
included in the library may be either a subset of the standard units provided
with GNAT Pro, or they may be specially tailored to the application.


.. _Run-Time_Libraries_and_Objects:

Run-Time Libraries and Objects
==============================

The run-time libraries implement functionality required by features
whose support is not provided by code generated directly by the compiler.
The complexity of the
run-time library depends on features used and kernel capabilities.

When an Ada program is built, the object code that makes
up the final executable may come from the following
entities (in addition to the user code itself):

* GNAT Pro run-time library
* C library
* Math library
* Internal GCC library
* Startup code

.. index:: -nostdlib (gcc)
.. index:: -nodefaultlibs (gcc)

The GNAT and GCC drivers automatically link all these libraries and
objects with the final executable, statically or dynamically depending
on the target and on some compilation options. The *-nostdlib*
and *-nodefaultlibs*
options may be used to control this automatic behavior.

GNAT Pro attempts to find these libraries and objects
in several standard system directories plus any that are
specified with the *-L* option or the ``LIBRARY_PATH``
environment variable.
The ``gcc --print-search-dirs`` command prints
the name of the configured installation directory and a list of
program and library directories where gcc will search.

The following sections define the contents and purpose of the various
elements potentially included in an application's executable.


.. index:: GNAT Pro Run-Time Library


.. _GNAT_Pro_Run-Time_Library:

GNAT Pro Run-Time Library
-------------------------

The high abstraction level and expressiveness provided by the full Ada
language requires a rather complex run-time library. This library
bridges the semantic gap between the high-level Ada constructs and the
low-level C functions and representations available in the target
system (in the form of C headers and libraries). Hence, the semantics
of Ada constructs are expanded into calls to a collection of lower-level
run-time constructions. An example of this is the implementation of Ada
tasking.

This GNAT Pro run-time library comprises both C and Ada files. The
C run-time files define a common low-level
interface that is implemented on top of the available C headers and
libraries in the underlying system. Ada packages within the GNAT Pro run-time
library implement the required Ada semantics.

In the case of certifiable systems, it is likely that almost no C files
are required.

The GNAT Pro run-time library depends of the following set of libraries:

* C Library (:file:`libc.a`) for a number of miscellaneous functions,
  such as the input/output system, memory management, etc.

* Math Library (:file:`libm.a`) for everything related to the
  functionality specified in the Ada Numerics Annex.

* Internal GCC Library (:file:`libgcc.a`) for features such as
  integer and floating point operations, and exception handling.


.. _C_Library:

C Library
---------

This library provides standard ANSI C functionality in the
form of:

* Standard Utility Functions (:file:`stdlib.h`)

* Character Type Macros and Functions (:file:`ctype.h`)

* Input and Output (:file:`stdio.h`)

* Strings and Memory (:file:`string.h`)

* Wide Character Strings (:file:`wchar.h`)

* Signal Handling (:file:`signal.h`)

* Time Functions (:file:`time.h`)

* Locale (:file:`locale.h`)

This C subroutine library depends on a few subroutine calls for
kernel or operating system services. If the C library is intended to
be used on a system that complies with the POSIX.1 standard (also
known as IEEE 1003.1), most of these subroutines are supplied with
the operating system or kernel.

For bare-board configurations
these subroutines are not provided with the system. For other
systems, only a fraction of these may be provided. In either case, the
user must provide, as a minimum, do-nothing stubs or subroutines with
the needed functionality, in order to allow the program to link
with the subroutines defined in :file:`libc.a`. Examples of primitives for which
``libc.a`` may be needed include:

+-----------------------------------+-------------------------+
| **Functionality**                 | **Routines**            |
+===================================+=========================+
| *Basic input/output capabilities* | ``open``, ``close``,    |
|                                   | ``read``, ``write``,    |
|                                   | ``stat``, ``fstat``,    |
|                                   | ``link``, ``unlink``,   |
|                                   | ``lseek``, ``isatty``   |
+-----------------------------------+-------------------------+
| *Accessing the environment*       | ``environ``             |
+-----------------------------------+-------------------------+
| *Process management*              | ``execve``, ``fork``,   |
|                                   | ``getpid``, ``times``,  |
|                                   | ``wait``, ``kill``,     |
|                                   | ``exit``                |
+-----------------------------------+-------------------------+
| *Heap management*                 | ``sbrk``                |
+-----------------------------------+-------------------------+

In the case of certifiable systems, most of these capabilities are
not needed. Hence, the recommended and simpler approach is that the
user implements (in Ada or C) just the required functionality, such
as:

+------------------------------------+-------------------------+
| **Functionality**                  | **Routines**            |
+====================================+=========================+
| *Simple Input/Output*              | ``read``, ``write``     |
+------------------------------------+-------------------------+
| *Basic memory operations*          | ``memcpy``, ``bcopy``,  |
|                                    | ``memmove``, ``memcmp`` |
+------------------------------------+-------------------------+
| *Dynamic memory (heap) management* | ``malloc``, ``free``    |
+------------------------------------+-------------------------+


.. _Math_Library:

Math Library
------------

A complete IEEE math library is usually provided by :file:`libm.a`, which
includes functions that take float, double, and long double
parameters. Depending on the type used the function has a different
extension. These extensions are named after their full precision
equivalents; i.e., ``sinf()`` is the single precision version of the
``sin()`` function, and ``sinl()`` is the long double
variant. The reduced precision functions run much faster than
their IEEE-compliant double precision counterparts,
which can make some floating point operations practical on hardware
that is too weak for full double precision computations.


.. _Internal_GCC_Library:

Internal GCC Library
--------------------

This is a library of internal subroutines that GCC uses to overcome
shortcomings of particular machines, or to satisfy the special needs of some
languages.

The contents of :file:`libgcc.a` are documented in the GCC internals manual and
may be inspected with standard binary oriented tools such as ``nm`` or
``objdump``. The whole set can be partitioned into the two
major groups that follow.


.. _Integer_and_Floating_Point_Operations:

Integer and Floating Point Operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This represents a fairly large set; documentation for most functions is
available in the GCC internals manual and in the GCC sources.
This section provides a brief introduction.

The names of these functions have the form ``__OpcodeModesNvalues``, where:

* *Opcode* specifies what the function does. E.g. ``mul`` for a
  multiplication, ``div`` for a division.

* *Modes* specifies the GCC machine mode of the operands it operates
  on. For example:

  * *si*: Single Integer (4bytes)
  * *di*: Double Integer (8bytes)
  * *sf*: Single Float (4bytes)
  * *df*: Double Float (8bytes)

* *Nvalues* specifies the number of values the function deals with,
  possibly including a result it computes.

Here are some examples:

* *__muldi3*: Multiply two DI integers and return the DI result


* *__negdi2*: Return the negation of a DI integer


* *__eqdf2*: Return zero if neither argument is NaN and the two
  (DF) arguments are equal


.. _Run-Time_Support_for_Exception_Handling_and_Trampolines:

Run-Time Support for Exception Handling and Trampolines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The low-level GCC library also includes everything potentially needed to
support a compiler configured to use the GCC scheme for exception
handling. These are the functions prefixed by
``_Unwind`` and ``__register_frame``.

Note that only some functions in this set are called
'implicitly'. Most are explicitly called from the regular run-time
libraries for exception-aware languages like C++ or Ada, when
configured to use the GCC scheme. Moreover, the High-Integrity Profiles
are not configured to use the GCC exception handling scheme (see
:ref:`Exceptions_and_the_High-Integrity_Profiles`, for details).

.. index:: Trampolines

In addition, *trampolines* (the GCC low-level mechanism to support
pointers to nested subprograms), may require several run-time routines to work
properly.

The compiler Back End will generate the necessary calls on routines such as
``__clear_cache`` and ``__trampoline_setup``

.. index:: No_Implicit_Dynamic_Code restrictions identifier

.. _Startup_Cleanup_Code:

``pragma Restriction (No_Implicit_Dynamic_Code)`` can be used to prohibit
pointers to nested subprograms, so that support for trampolines
is not required in that case.


Startup / Cleanup Code
----------------------

The startup / cleanup code is usually found in assembly files named
:file:`crt*.S` (*crt* stands for 'C Run Time').
Their objects are linked at the
beginning and at the end of the executable. Their purpose is:

* to perform required program initialization (e.g., initialize hardware,
  reserve space for stack, zeroing the ``.bss`` section),

* to bootstrap the rest of the application, and

* to arrange the necessary 'cleanup' / finalization after program
  execution completes.


The :file:`crt0` file defines a special symbol like ``_start`` that is both
the default base address for the application and the first symbol in the
executable binary image.

The :file:`crt*.S` files are normally provided by the operating system.
In a bare-board configuration it is usually the case that only the initial
startup code (such as :file:`crt0.S`) is needed, and must be provided by
the user.


.. _How_Object_Dependencies_are_Generated:

How Object Dependencies are Generated
=====================================


.. _Explicit_With_Clauses:

Explicit ``with`` Clauses
-------------------------

The use of ``with`` clauses creates a dependence relationship between Ada
units. This relationship is computed at compilation time and recorded in
the :file:`ali` file produced for each object. The final executable will
contain all the objects corresponding to the units in the dependence
closure of the main unit.

This is the simplest and most common way of determining the required
set of objects in the final application.


.. _Compiler-Generated_Calls_to_GNAT_Pro_Run-Time_Primitives:

Compiler-Generated Calls to GNAT Pro Run-Time Primitives
--------------------------------------------------------

.. index:: -gnatD (gcc)
.. index:: -gnatG (gcc)

When an Ada source file is compiled, the GNAT Pro compiler Front End
generates an
intermediate representation of the original source code. This is an
expanded low-level version of the original source code that can be
displayed in an
Ada-like format, and can be inspected using the ``-gnatD`` or
``-gnatG`` compiler switch.

The expanded code contains calls to the run-time primitives
that implement different Ada features. The required run-time library
packages are linked to the included hierarchy of library units, in the
same way as if an explicit ``with`` had been used. These
dependencies on the GNAT Pro run-time units are also determined at
compilation time.


.. _Pragma_Import:

Pragma Import
-------------

A pragma Import specifies that the designated entity is defined
externally. The use of ``pragma Import`` clauses forces the inclusion of
the required external symbol (and transitively, those that it requires) in the
resulting executable file. This dependency is resolved at link time,
because it is not possible to know in advance which object file
contains the required symbol.

The fact that this dependence is resolved late (at link time, after
the binder file has been generated) has a potentially
dangerous effect: when an Ada subprogram is imported, the binder does
not know where the symbol comes from, and the
elaboration code that the imported routine may require will not be called.


.. _Back-End_Generated_Calls_to_Library_Functions:

Back-End Generated Calls to Library Functions
---------------------------------------------

The GCC back-end may generate 'implicit' calls to library subprograms
for various reasons. Such calls are said to be implicit because they
do not directly correspond to explicit subprogram invocations in the
application source code.

Implicit calls to library subprograms occur for several reasons:

(a) *Integer and floating point operations*. Some source operations
    require arithmetic support not available on the target hardware.

(b) *Run-time support for exception handling and trampolines*. Some
    high-level constructs require low-level data structure management too
    complex to emit inline code for.

(c) *Basic memory operations*. Some basic memory operations are too
    expensive to expand inline, e.g. large block copies or comparisons.

For (a), what the compiler knows about the target hardware may
depend on compilation options. For instance, ``-msoft-float`` triggers
calls to library functions for floating point operations even if the
hardware has the necessary instructions available. Similarly, the
``-mcpu`` switch allows modifying the compiler's default view of the
target hardware.

The functions to support (a) and (b) are located in :file:`libgcc.a`, the GCC
low-level runtime library built together with the compiler itself.

For (c), the called functions are located in the regular system C
library, except for the block comparison function on systems where
``memcmp`` is not available, in which case, the libgcc
``__gcc_bcmp`` function is used.

Note that each toolchain is configured for a particular set of core
cpus, and not all combinations of ``-mcpu`` or ``-msoft-float`` switches
are supported. For instance, support for the e500v2 powerpc core requires a
different toolchain than the default powerpc one.


.. _How_The_Run_Time_Library_Is_Configured:

How The Run Time Library Is Configured
======================================

There are three major mechanisms for tailoring the run-time library.

* Use of Configuration Pragmas
* Specification of Configuration Parameters
* Restricting the Set of Run-Time Units

These three mechanisms work together to provide a coherent run-time library
that provides a well defined subset. The compiler understands
these mechanisms, and will properly enforce the corresponding language
subset, providing informative and appropriate messages if features not
supported by the subset are used.


.. index:: Configuration pragmas (for tailoring the run time)

.. _Use_of_Configuration_Pragmas:

Use of Configuration Pragmas
----------------------------

A selected set of configuration pragmas can be placed at the start of package
``System``, and enforced for all units compiled in the presence of this
``System`` package:

.. index:: pragma Detect_Blocking
.. index:: pragma Discard_Names
.. index:: pragma Locking_Policy
.. index:: pragma Normalize_Scalars
.. index:: pragma Polling
.. index:: pragma Queuing_Policy
.. index:: pragma Task_Dispatching_Policy

.. code-block:: ada

     pragma Detect_Blocking;
     pragma Discard_Names;
     pragma Locking_Policy (name);
     pragma Normalize_Scalars;
     pragma Polling (On);
     pragma Queuing_Policy (name);
     pragma Task_Dispatching_Policy (name);

The units provided in the corresponding run-time library
need not support language features that would be prohibited by these pragmas.

.. index:: pragma Restrictions

In addition, ``Restrictions`` pragmas
may be used for all simple
restrictions which are required to be applied consistently throughout
a partition.
The current set of such restrictions is given in the following list.
GNAT Pro implements all such restrictions defined in the Ada RM,
and, in the list below,
the RM reference is given for these restrictions. In addition, GNAT Pro also
implements a number of implementation-defined restrictions. See the
:title:`GNAT Reference Manual` for details of the meaning of these additional
restrictions. This list is taken from the run-time source file
:file:`s-rident.ads`, which should be consulted for the definitive
current list for your configuration.

.. code-block:: ada

        Boolean_Entry_Barriers,                  -- GNAT (Ravenscar)
        No_Abort_Statements,                     -- (RM D.7(5), H.4(3))
        No_Access_Subprograms,                   -- (RM H.4(17))
        No_Allocators,                           -- (RM H.4(7))
        No_Asynchronous_Control,                 -- (RM D.7(10))
        No_Calendar,                             -- GNAT
        No_Delay,                                -- (RM H.4(21))
        No_Direct_Boolean_Operators,             -- GNAT
        No_Dispatch,                             -- (RM H.4(19))
        No_Dynamic_Interrupts,                   -- GNAT
        No_Dynamic_Priorities,                   -- (RM D.9(9))
        No_Enumeration_Maps,                     -- GNAT
        No_Entry_Calls_In_Elaboration_Code,      -- GNAT
        No_Entry_Queue,                          -- GNAT (Ravenscar)
        No_Exception_Handlers,                   -- GNAT
        No_Exception_Registration,               -- GNAT
        No_Exceptions,                           -- (RM H.4(12))
        No_Finalization,                         -- GNAT
        No_Fixed_Point,                          -- (RM H.4(15))
        No_Floating_Point,                       -- (RM H.4(14))
        No_IO,                                   -- (RM H.4(20))
        No_Implicit_Conditionals,                -- GNAT
        No_Implicit_Dynamic_Code,                -- GNAT
        No_Implicit_Heap_Allocations,            -- (RM D.8(8), H.4(3))
        No_Implicit_Loops,                       -- GNAT
        No_Initialize_Scalars,                   -- GNAT
        No_Local_Allocators,                     -- (RM H.4(8))
        No_Local_Protected_Objects,              -- GNAT
        No_Nested_Finalization,                  -- (RM D.7(4))
        No_Protected_Type_Allocators,            -- GNAT
        No_Protected_Types,                      -- (RM H.4(5))
        No_Recursion,                            -- (RM H.4(22))
        No_Reentrancy,                           -- (RM H.4(23))
        No_Relative_Delay,                       -- GNAT (Ravenscar)
        No_Requeue,                              -- GNAT
        No_Secondary_Stack,                      -- GNAT
        No_Select_Statements,                    -- GNAT (Ravenscar)
        No_Standard_Storage_Pools,               -- GNAT
        No_Streams,                              -- GNAT
        No_Task_Allocators,                      -- (RM D.7(7))
        No_Task_Attributes,                      -- GNAT
        No_Task_Hierarchy,                       -- (RM D.7(3), H.4(3))
        No_Task_Termination,                     -- GNAT (Ravenscar)
        No_Tasking,                              -- GNAT
        No_Terminate_Alternatives,               -- (RM D.7(6))
        No_Unchecked_Access,                     -- (RM H.4(18))
        No_Unchecked_Conversion,                 -- (RM H.4(16))
        No_Unchecked_Deallocation,               -- (RM H.4(9))
        No_Wide_Characters,                      -- GNAT
        Static_Priorities,                       -- GNAT
        Static_Storage_Size,                     -- GNAT

        Max_Asynchronous_Select_Nesting,         -- (RM D.7(18), H.4(3))
        Max_Entry_Queue_Depth,                   -- GNAT
        Max_Protected_Entries,                   -- (RM D.7(14))
        Max_Select_Alternatives,                 -- (RM D.7(12))
        Max_Storage_At_Blocking,                 -- (RM D.7(17))
        Max_Task_Entries,                        -- (RM D.7(13), H.4(3))
        Max_Tasks,                               -- (RM D.7(19), H.4(3))


No other pragmas are allowed in package ``System`` (other than the pragma
``Pure`` for ``System`` itself which is always present).


.. _Specification_of_Configuration_Parameters:

Specification of Configuration Parameters
-----------------------------------------

The private part of package ``System`` defines a number of Boolean
configuration switches, which control the support of specific language
features.

  .. index:: Backend_Divide_Checks (configuration parameter)
  .. index:: Backend_Overflow_Checks (configuration parameter)
  .. index:: Front-End longjmp/setjmp exceptions
  .. index:: Configurable_Run_Time (configuration parameter)
  .. index:: Back-End zero cost exceptions
  .. index:: ZCX_By_Default (configuration parameter)
  .. index:: Suppress_Standard_Library (configuration parameter)
  .. index:: Duration_32_Bits (configuration parameter)
  .. index:: Support_Aggregates (configuration parameter)
  .. index:: Support_Composite_Assign (configuration parameter)
  .. index:: Support_Composite_Compare (configuration parameter)
  .. index:: Support_Long_Shifts (configuration parameter)
  .. index:: Stack_Check_Probes (configuration parameter)
  .. index:: Stack_Check_Default (configuration parameter)
  .. index:: Command_Line_Args (configuration parameter)
  .. index:: Exit_Status_Supported (configuration parameter)
  .. index:: Use_Ada_Main_Program_Name (configuration parameter)
  .. index:: Denorm (configuration parameter)
  .. index:: Machine_Rounds (configuration parameter)
  .. index:: Machine_Overflows (configuration parameter)
  .. index:: Signed_Zeros (configuration parameter)
  .. index:: OpenVMS (configuration parameter)
  .. index:: Fractional_Fixed_Ops (configuration parameter)
  .. index:: Functions_Return_By_DSP (configuration parameter)
  .. index:: Frontend_Layout (configuration parameter)
  .. index:: Preallocated_Stacks (configuration parameter)

.. code-block:: ada

     -----------------------
     -- Target Parameters --
     -----------------------

     --  The following parameters correspond to the constants defined in the
     --  private part of System. Note that it is required that all parameters
     --  defined here be specified in the target specific version of system.ads
     --  There are no default values.

     -------------------------------
     -- Backend Arithmetic Checks --
     -------------------------------

     --  Divide and overflow checks are either done in the front end or
     --  back end. The front end will generate checks when required unless
     --  the corresponding parameter here is set to indicate that the back
     --  end will generate the required checks (or that the checks are
     --  automatically performed by the hardware in an appropriate form).

     Backend_Divide_Checks : Boolean;

     --  Set True if the back end generates divide checks, or if the hardware
     --  checks automatically. Set False if the front end must generate the
     --  required tests using explicit expanded code.

     Backend_Overflow_Checks : Boolean;

     --  Set True if the back end generates arithmetic overflow checks, or if
     --  the hardware checks automatically. Set False if the front end must
     --  generate the required tests using explicit expanded code.

     -----------------------------------
     -- Control of Exception Handling --
     -----------------------------------

     --  GNAT implements two methods of implementing exceptions:

     --    Front-End Longjmp/Setjmp Exceptions

     --      This approach uses longjmp/setjmp to handle exceptions. It
     --      uses less storage, and can often propagate exceptions faster,
     --      at the expense of (sometimes considerable) overhead in setting
     --      up an exception handler. This approach is available on all
     --      targets, and is the default where it is the only approach.

     --      The generation of the setjmp and longjmp calls is handled by
     --      the front end of the compiler (this includes gigi in the case
     --      of the standard GCC back end). It does not use any back end
     --      support (such as the GCC3 exception handling mechanism). When
     --      this approach is used, the compiler generates special exception
     --      handlers for handling cleanups when an exception is raised.

     --    Back-End Zero Cost Exceptions

     --      With this approach, the back end handles the generation and
     --      handling of exceptions. For example, the GCC3 exception handling
     --      mechanisms are used in this mode. The front end simply generates
     --      code for explicit exception handlers, and AT END cleanup handlers
     --      are simply passed unchanged to the backend for generating cleanups
     --      both in the exceptional and non-exceptional cases.

     --      As the name implies, this approach generally uses a zero-cost
     --      mechanism with tables, but the tables are generated by the back
     --      end. However, since the back-end is entirely responsible for the
     --      handling of exceptions, another mechanism might be used. In the
     --      case of GCC3 for instance, it might be the case that the compiler
     --      is configured for setjmp/longjmp handling, then everything will
     --      work correctly. However, it is definitely preferred that the
     --      back end provide zero cost exception handling.

     --    Control of Available Methods and Defaults

     --      The following switches specify whether the ZCX method is
     --      available in an implementation, and which method is the default
     --      method.

     ZCX_By_Default : Boolean;

     --  Indicates if zero cost exceptions are active by default. If this
     --  variable is False, then the only possible exception method is the
     --  front-end setjmp/longjmp approach, and this is the default. If
     --  this variable is True, then one of the following two flags must
     --  be True, and represents the method to be used by default.

    --------------------------------
     -- Configurable Run-Time Mode --
     --------------------------------

     --  In configurable run-time mode, the system run-time may not support
     --  the full Ada language. The effect of setting this switch is to let
     --  the compiler know that it is not surprising (i.e. the system is not
     --  misconfigured) if run-time library units or entities within units are
     --  not present in the run-time.

     Configurable_Run_Time_On_Target : Boolean;

     --  Indicates that the system.ads file is for a configurable run-time
     --
     --  This has some specific effects as follows
     --
     --    The binder generates the gnat_argc/argv/envp variables in the
     --    binder file instead of being imported from the run-time library.
     --    If Command_Line_Args_On_Target is set to False, then the
     --    generation of these variables is suppressed completely.
     --
     --    The binder generates the gnat_exit_status variable in the binder
     --    file instead of being imported from the run-time library. If
     --    Exit_Status_Supported_On_Target is set to False, then the
     --    generation of this variable is suppressed entirely.
     --
     --    The routine __gnat_break_start is defined within the binder file
     --    instead of being imported from the run-time library.
     --
     --    The variable __gnat_exit_status is generated within the binder file
     --    instead of being imported from the run-time library.

     Suppress_Standard_Library : Boolean;

     --  If this flag is True, then the standard library is not included by
     --  default in the executable (see unit System.Standard_Library in file
     --  s-stalib.ads for details of what this includes). This is for example
     --  set True for the Zero Footprint case, where these files should not
     --  be included by default.
     --
     --  This flag has some other related effects:
     --
     --    The generation of global variables in the bind file is suppressed,
     --    with the exception of the priority of the environment task, which
     --    is needed by the Ravenscar run-time.
     --
     --    The generation of exception tables is suppressed for front end
     --    ZCX exception handling (since we assume no exception handling).
     --
     --    The calls to __gnat_initialize and __gnat_finalize are omitted
     --
     --    All finalization and initialization (controlled types) is omitted
     --
     --    The routine __gnat_handler_installed is not imported

     ---------------------
     -- Duration Format --
     ---------------------

     --  By default, type Duration is a 64-bit fixed-point type with a delta
     --  and small of 10**(-9) (i.e. it is a count in nanoseconds. This flag
     --  allows that standard format to be modified.

     Duration_32_Bits : Boolean;

     --  If True, then Duration is represented in 32 bits and the delta and
     --  small values are set to 20.0*(10**(-3)) (i.e. it is a count in units
     --  of 20 milliseconds).

     ------------------------------------
     -- Back-End Code Generation Flags --
     ------------------------------------

     --  These flags indicate possible limitations in what the code generator
     --  can handle. They will all be True for a full run-time, but one or more
     --  of these may be false for a configurable run-time, and if a feature is
     --  used at the source level, and the corresponding flag is false, then an
     --  error message will be issued saying the feature is not supported.

     Support_Aggregates : Boolean;

     --  In the general case, the use of aggregates may generate calls
     --  to run-time routines in the C library, including memset, memcpy,
     --  memmove, and bcopy. This flag is set to True if these routines
     --  are available. If any of these routines is not available, then
     --  this flag is False, and the use of aggregates is not permitted.

     Support_Composite_Assign : Boolean;

     --  The assignment of composite objects other than small records and
     --  arrays whose size is 64-bits or less and is set by an explicit
     --  size clause may generate calls to memcpy, memmove, and bcopy.
     --  If versions of all these routines are available, then this flag
     --  is set to True. If any of these routines is not available, then
     --  the flag is set False, and composite assignments are not allowed.

     Support_Composite_Compare : Boolean;

     --  If this flag is True, then the back end supports bit-wise comparison
     --  of composite objects for equality, either generating inline code or
     --  calling appropriate (and available) run-time routines. If this flag
     --  is False, then the back end does not provide this support, and the
     --  front end uses component by component comparison for composites.

     Support_Long_Shifts : Boolean;

     --  If True, the back end supports 64-bit shift operations. If False, then
     --  the source program may not contain explicit 64-bit shifts. In addition,
     --  the code generated for packed arrays will avoid the use of long shifts.

     -------------------------------
     -- Control of Stack Checking --
     -------------------------------

     --  GNAT provides two methods of implementing exceptions:

     --    GCC Probing Mechanism

     --      This approach uses the standard GCC mechanism for
     --      stack checking. The method assumes that accessing
     --      storage immediately beyond the end of the stack
     --      will result in a trap that is converted to a storage
     --      error by the runtime system. This mechanism has
     --      minimal overhead, but requires complex hardware,
     --      operating system and run-time support. Probing is
     --      the default method where it is available. The stack
     --      size for the environment task depends on the operating
     --      system and cannot be set in a system-independent way.

     --   GNAT Stack-limit Checking

     --      This method relies on comparing the stack pointer
     --      with per-task stack limits. If the check fails, an
     --      exception is explicitly raised. The advantage is
     --      that the method requires no extra system dependent
     --      runtime support and can be used on systems without
     --      memory protection as well, but at the cost of more
     --      overhead for doing the check. This method is the
     --      default on systems that lack complete support for
     --      probing.

     Stack_Check_Probes : Boolean;

     --  Indicates if stack check probes are used, as opposed to the standard
     --  target independent comparison method.

     Stack_Check_Default : Boolean;

     --  Indicates if stack checking is on by default

     ----------------------------
     -- Command Line Arguments --
     ----------------------------

     --  For most ports of GNAT, command line arguments are supported. The
     --  following flag is set to False for targets that do not support
     --  command line arguments (VxWorks). Note that support of command line
     --  arguments is not required on such targets (RM A.15(13)).

     Command_Line_Args : Boolean;

     --  Set False if no command line arguments on target

     --  Similarly, most ports support the use of an exit status, but some
     --  ports may not (as allowed by RM A.15(18-20))

     Exit_Status_Supported : Boolean;

     --  Set False if returning of an exit status is not supported on target

     -----------------------
     -- Main Program Name --
     -----------------------

     --  When the binder generates the main program to be used to create the
     --  executable, the main program name is ``main`` by default (to match the
     --  usual Unix practice). If this parameter is set to True, then the
     --  name is instead by default taken from the actual Ada main program
     --  name (just the name of the child if the main program is a child unit).
     --  In either case, this value can be overridden using -M name.

     Use_Ada_Main_Program_Name : Boolean;

     --  Set True to use the Ada main program name as the main name

     ----------------------------------------------
     -- Boolean-Valued Floating-Point Attributes --
     ----------------------------------------------

     --  The constants below give the values for representation oriented
     --  floating-point attributes that are the same for all float types
     --  on the target. These are all boolean values.

     --  A value is only True if the target reliably supports the corresponding
     --  feature. Reliably here means that support is guaranteed for all
     --  possible settings of the relevant compiler switches (like -mieee),
     --  since we cannot control the user setting of those switches.

     --  The attributes cannot dependent on the current setting of compiler
     --  switches, since the values must be static and consistent throughout
     --  the partition. We probably should add such consistency checks in future,
     --  but for now we don't do this.

     Denorm : Boolean;

     --  Set to False on targets that do not reliably support denormals.
     --  Reliably here means for all settings of the relevant -m flag, so
     --  for example, this is False on the Alpha where denormals are not
     --  supported unless -mieee is used.

     Machine_Rounds : Boolean;

     --  Set to False for targets where S'Machine_Rounds is False

     Machine_Overflows : Boolean;

     --  Set to True for targets where S'Machine_Overflows is True

     Signed_Zeros : Boolean;

     --  Set to False on targets that do not reliably support signed zeros.

     OpenVMS : Boolean;

     --  Set to True if target is OpenVMS.

     -------------------------------------------
     -- Boolean-Valued Fixed-Point Attributes --
     -------------------------------------------

     Fractional_Fixed_Ops : Boolean;

     --  Set to True for targets that support fixed-by-fixed multiplication
     --  and division for fixed-point types with a small value equal to
     --  2 ** (-(T'Object_Size - 1)) and whose values have an absolute
     --  value less than 1.0.

     --------------------------------------------------------------
     -- Handling of Unconstrained Values Returned from Functions --
     --------------------------------------------------------------

     --  Functions that return variable length objects, notably unconstrained
     --  arrays are a special case, because there is no simple obvious way of
     --  implementing this feature. Furthermore, this capability is not present
     --  in C++ or C, so typically the system ABI does not handle this case.

     --  GNAT uses two different approaches

     --    The Secondary Stack

     --      The secondary stack is a special storage pool that is used for
     --      this purpose. The called function places the result on the
     --      secondary stack, and the caller uses or copies the value from
     --      the secondary stack, and pops the secondary stack after the
     --      value is consumed. The secondary stack is outside the system
     --      ABI, and the important point is that although generally it is
     --      handled in a stack like manner corresponding to the subprogram
     --      call structure, a return from a function does NOT pop the stack.

     --    DSP (Depressed Stack Pointer)

     --      Some targets permit the implementation of a function call/return
     --      protocol in which the function does not pop the main stack pointer
     --      on return, but rather returns with the stack pointer depressed.
     --      This is not generally permitted by any ABI, but for at least some
     --      targets, the implementation of alloca provides a model for this
     --      approach. If return-with-DSP is implemented, then functions that
     --      return variable length objects do it by returning with the stack
     --      pointer depressed, and the returned object is a pointer to the
     --      area within the stack frame of the called procedure that contains
     --      the returned value. The caller must then pop the main stack when
     --      this value is consumed.

     Functions_Return_By_DSP : Boolean;

     --  Set to True if target permits functions to return with using the
     --  DSP (depressed stack pointer) approach.

     -----------------
     -- Data Layout --
     -----------------

     --  Normally when using the GCC backend, Gigi and GCC perform much of the
     --  data layout using the standard layout capabilities of GCC. If the
     --  parameter Backend_Layout is set to False, then the front end must
     --  perform all data layout. For further details see the package Layout.

     Frontend_Layout : Boolean;

     --  Set True if front end does layout

     -------------------------------
     -- Control of Stack Creation --
     -------------------------------

     --  In bare-board configurations supporting a static task model (such as
     --  Ravenscar), the compiler can create statically (at compile time) the
     --  stacks to be used by the different tasks.

     Preallocated_Stacks : Boolean;

     --  Set to True if the compiler creates statically the stacks for the
     --  different tasks. Set to False if stacks are created by the underlying
     --  operating system at run time.


.. _Restricting_the_Set_of_Run-Time_Units:

Restricting the Set of Run-Time Units
-------------------------------------

Many Ada language features generate implicit calls to the run-time library.
For example, if we have the Ada procedure:

.. code-block:: ada

   pragma Suppress (All_Checks);
   function Calc (X : Integer) return Integer is
   begin
      return X ** 4 + X ** 52;
   end Calc;

Then the compiler will generate the following code (this is *-gnatG*
output):

::

  with system.system__exn_int;

  function calc (x : integer) return integer is
  begin
     E1b : constant integer := x * x;
     return integer (E1b * E1b +
                      integer(system__exn_int__exn_integer (x, 52)));
  end calc;

.. index:: Exponentiation (and configurable run-time)

In the generated code, you can see that the compiler generates direct inlined
code for ``X ** 4`` (by computing ``(X ** 2) ** 2``).
But the computation of ``X ** 52``
requires a call to the runtime routine ``System.Exn_Int.Exn_Integer``
(the double underlines in the *-gnatG* output represent dots in the
name).

The full GNAT Pro run-time library contains an appropriate package that
provides this capability:

.. code-block:: ada

   --  Integer exponentiation (checks off)

   package System.Exn_Int is
   .. index:: ``System.Exn_Int`` package

   pragma Pure (Exn_Int);

      function Exn_Integer
        (Left  : Integer;
         Right : Natural)
         return  Integer;

   end System.Exn_Int;

.. index:: Configurable_Run_Time (in package System)

If the configurable run-time option is chosen
(set ``Configurable_Run_Time``
to ``True`` in the ``System`` spec
in file :file:`system.ads`), then package ``System.Exn_Int`` may or may
not be present in the run-time library. If it is not present, then the subset
of Ada does not allow exponentiation by large integer values, and an attempt
to compile ``Calc`` will result in an error message:

::

  1. function Calc (X : Integer) return Integer is
  2. begin
  3.   return X ** 4 + X ** 52;
                         |
     >>> construct not allowed in this configuration
     >>> entity "System.Exn_Int.Exn_Integer" not defined

  4. end Calc;

The first line of the error message indicates that the construct is
not provided in the library. The second line shows the exact entity
that is missing. In this case, it is the entity ``Exn_Integer``
in package ``System.Exn_Int``. This package is in file
``s-exnint.ads`` (you can use the command
``gnatkr system.exn_int.ads`` to find this file name).
If you look at the spec of this package, you will find the
specification of this function:

.. code-block:: ada

   function Exn_Integer
    (Left : Integer; Right : Natural) return Integer;

If exponentiation is required, then this package must be provided,
and must contain an appropriate declaration of the missing entity. There are
two ways to accomplish this. Either the standard GNAT body can be
copied and used in the configurable run-time, or a new body can be written
that satisfies the specification. Rewriting the body may be useful either
to simplify the implementation (possibly taking advantage of configuration
pragmas provided in :file:`system.ads`), or to meet coding requirements of some
particular certification protocol.

In either case, you will have to prepare certification materials
for the new package, since the existing certification materials
for the run-time library will not include this new package.

Alternatively, you could modify the source code to call an
exponentiation routine that is defined within your application:

.. code-block:: ada

   with Exp;
   function Calc (X : Integer) return Integer is
   begin
     return Exp (X, 4) + Exp (X, 52);
   end Calc;

where ``Exp`` is an application function that provides the desired
exponentiation capability, and is certified along with the rest of the
application in the normal manner.

There are several hundred similar units in the library. For each unit, the
unit may or may not be present in the configurable run-time, depending on
which facilities are required.


.. index:: Naming the run-time library

.. _Naming_the_Run-Time_Library:

Naming the Run-Time Library
===========================

To assist in keeping track of multiple run-time configurations,
GNAT Pro Safety-Critical and GNAT Pro High-Security provide a facility
for naming the run-time library. To do this,
include a line with the following format (starting in column 4) in
:file:`system.ads`:

.. index:: Run_Time_Name (for configurable run time)

.. code-block:: ada

     Run_Time_Name : constant String := "Simple Run Time 1";

The name may contain letters, digits, spaces and underlines. If such a name
is provided, then error messages pertaining to the subset include the name
of the library:

::

  1. function Calc (X : Integer) return Integer is
  2. begin
  3.   return X ** 4 + X ** 52;
                         |
     >>> construct not allowed in this configuration (Simple Run Time 1)

  4. end Calc;


Configuring a Special Purpose Library
=====================================

As described above, the run-time library may be tailored to suit a specific
application. This process can be carried out either by augmenting an existing
restricted run-time library implementation, or by reducing an existing "full"
library.

A small set of standard units is supplied which can be added to the Zero
Footprint library to expand the supported subset, including:

  .. index:: Secondary Stack Support

* *Secondary Stack Support*

  This allows functions to return unconstrained results, e.g. arbitrary
  length strings.

  .. index:: Minimal Exception Support

* *Minimal Exception Support*

  This allows for a minimal support for propagation of exceptions

It is of course possible to add any units. However, the configuration of
a complex run-time library may be quite difficult, and is best carried out
in consultation with experts who are familiar with the structure of the
GNAT run-time libraries.

Adding the certifiable math library is a good example of a reasonable
configuration for a user. Specifically,
``Ada.Numerics.Generic_Elementary_Functions``
and language-defined instantiations can be added to a run-time that does not
already include them.  Doing so will add the following tailored Ada units:

* ``Ada.Numerics``
* ``Ada.Numerics.Generic_Elementary_Functions``
* ``Ada.Numerics.Elementary_Functions``
* ``Ada.Numerics.Long_Elementary_Functions``
* ``Ada.Numerics.Long_Long_Elementary_Functions``

To add them to a library, you copy the necessary sources to the intended
run-time library and build the library.

We will illustrate the configuration steps by adding the certifiable math
library to the ZFP run-time library for the STM32F4 ARM platform. (That
library and platform are arbitrary choices.)

A simple, clean approach is to create a distinct new library as a copy of an
existing run-time library implementation. Therefore we copy the run-time library
located in a directory named "zfp-stm32f4" under the compiler's installation.
This directory, along with those for the other run-time libraries,
is located under the ``<platform-name>/lib/gnat/`` directory. The "zfp-stm32f4"
runtime is for an ARM target, so "platform-name" is "arm-eabi" in this case.

For example, on Windows, and assuming the default location, this existing run-time
library implementation would be in the following directory:

::

   C:\GNATPRO\7.4.0\arm-eabi\lib\gnat\zfp-stm32f4\

Be sure to copy one of the directories under the ``<platform-name>/lib/gnat/``
directory. There are other directories, elsewhere under the GNAT Pro
installation, that have the same run-time library names but that are not the
run-time library implementations. You should see files named
:file:`runtime_build.gpr` and
:file:`runtime.xml` for example, among others.

The ultimate location for the library copy is an arbitrary choice, but note that
if you place it with the other predefined libraries, under the existing GNAT Pro
installation hierarchy, you will be able to reference it more conveniently. That
is because the tools will search for the library in that location, and as a
result the full path will not be required.

For illustration we will name the new library "zfp-stm32f4-math" and so that will
be the name of the run-time root directory as well.

There is a subdirectory specifically intended for the math library source files.
This subdirectory is appropriately named "math" and is located under the root of
the run-time library directory. The directory is empty in those run-times that
do not include the certifiable math library by default. However, for those
run-times that do provide the math library, the source files will be present.
The source files are included in the "ravenscar-full-stm32f4" run-time
library, for example.

Therefore, copy the following source files into the new, empty "math"
subdirectory:

* :file:`a-ngelfu.adb`
* :file:`a-ngelfu.ads`
* :file:`a-nlelfu.ads`
* :file:`a-nllefu.ads`
* :file:`a-nuelfu.ads`
* :file:`a-numaux.ads`
* :file:`a-numeri.ads`
* :file:`s-gcmain.adb`
* :file:`s-gcmain.ads`
* :file:`s-libdou.adb`
* :file:`s-libdou.ads`
* :file:`s-libm.adb`
* :file:`s-libm.ads`
* :file:`s-libsin.adb`
* :file:`s-libsin.ads`
* :file:`s-lidosq.adb`
* :file:`s-lidosq.ads`
* :file:`s-lisisq.adb`
* :file:`s-lisisq.ads`

Do not copy all the source files located in the full run-time's
"math" directory. Only copy those listed above.

Once the sources are copied you are ready to build the new run-time library. The
"math" directory, although initially empty, is already defined as a source
directory in the GNAT project file (gpr file) used to build the library.

To build, open a command line shell in the root of the new run-time directory
tree and invoke gprbuild as follows:

::

   gprbuild --target=arm-eabi -P runtime_build.gpr

You will see the new math sources compiled (along with a few others) and the new
library archive file created.

We specified the target on the invocation to gprbuild as "arm-eabi" since that
corresponds to the STM32F4. Change it if necessary for your platform.

Note that other parameters can also be specified on the invocation, for example
the kind of board targeted.  See the files named :file:`runtime.xml` in the roots
of the run-time library directories for these scenario variables.

The new certifiable math library is now available to applications building against
the "zfp-stm32f4-math" run-time library. You can specify the path to the new
run-time directory in the project file via the Runtime attribute, or on the command
line via the ``--RTS`` switch.
