------------------------------------------------------------------------------
--                                                                          --
--                          ESA RAVENSCAR BENCHMARK                         --
--                                                                          --
--                          H L _ T _ A _ 0 2 . A D B                       --
--                                                                          --
--                                 B o d y                                  --
--                                                                          --
--               Copyright (C) 2004 The European Space Agency               --
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

with Support_Timing;       use Support_Timing;
with Support_Base;  use Support_Base;
with Support_Types; use Support_Types;

procedure hl_t_a_02a is

   pragma Optimize (Time);

   E1             : Support_Types.Vector (Integer16'(1) .. Integer16'(4));
   X1, X2, X3, X4 : Float6;
   -- variables get munged in module 1
   X, Y, Z : Float6;
   T       : constant Float6 := 0.499975;
   T1      : constant Float6 := 0.50025;
   T2      : constant Float6 := 2.0;
   J, K, L : Integer16 range 1 .. 3;
   J2      : Integer16 range 0 .. 3;
   J1      : Integer16 range 2 .. 5;
   K1      : Integer16 range 3 .. 8;

   Kw : constant := 1000;

   N1  : constant Integer16 := Integer16 (0.0 * Kw);
   N2  : constant Integer16 := Integer16 (0.12 * Kw);
   N3  : constant Integer16 := Integer16 (0.14 * Kw);
   N4  : constant Integer16 := Integer16 (3.45 * Kw);
   N6  : constant Integer16 := Integer16 (2.1 * Kw);
   N7  : constant Integer16 := Integer16 (0.32 * Kw);
   N8  : constant Integer16 := Integer16 (8.99 * Kw);
   N9  : constant Integer16 := Integer16 (6.16 * Kw);
   N10 : constant Integer16 := Integer16 (0.0 * Kw);
   N11 : constant Integer16 := Integer16 (0.93 * Kw);

   procedure Pa (E : in out Support_Types.Vector) is
      J : Integer16;
   begin
      J := 0;
      <<Lab>>E (1) := (E (1) + E (2) + E (3) - E (4)) * T;
      E (2) := (E (1) + E (2) - E (3) + E (4)) * T;
      E (3) := (E (1) - E (2) + E (3) + E (4)) * T;
      E (4) := (-E (1) + E (2) + E (3) + E (4)) / T2;
      J := J + 1;
      if J < 6 then
         goto Lab;
      end if;
   end Pa;

   procedure P0 is
   begin
      E1 (J) := E1 (K);
      E1 (K) := E1 (L);
      E1 (L) := E1 (J);
   end P0;

   procedure P3 (X_In, Y_In : in Float6; Z : out Float6) is
      X : Float6 := X_In;  -- simulate Algol
      Y : Float6 := Y_In;  -- value parameter
   begin
      X := T * (X + Y);
      Y := T * (X + Y);
      Z := (X + Y) / T2;
   end P3;

begin

   X1 := +1.0;
   X2 := -1.0;
   X3 := -1.0;
   X4 := -1.0;

   --  <init_variables>
 --  <start_comment>
 --  Single precision whetstone benchmark with optimize (Time)
 --  <end_comment>
   --  <start_measure>
   -- module 1 : simple identifiers
   -- ========

   for I in  1 .. N1 loop
      X1 := (X1 + X2 + X3 - X4) * T;
      X2 := (X1 + X2 - X3 + X4) * T;
      X3 := (X1 - X2 + X3 + X4) * T;
      X4 := (-X1 + X2 + X3 + X4) * T;
   end loop;

   if N1 /= 0 and then X3 < -0.75 then
      raise Program_Error;
   end if;

   -- module 2: array elements
   -- ========

   E1 (1) := 1.0;
   E1 (2) := -1.0;
   E1 (3) := -1.0;
   E1 (4) := -1.0;
   for I in  1 .. N2 loop
      E1 (1) := (E1 (1) + E1 (2) + E1 (3) - E1 (4)) * T;
      E1 (2) := (E1 (1) + E1 (2) - E1 (3) + E1 (4)) * T;
      E1 (3) := (E1 (1) - E1 (2) + E1 (3) + E1 (4)) * T;
      E1 (4) := (-E1 (1) + E1 (2) + E1 (3) + E1 (4)) * T;
   end loop;

   if N2 /= 0 and then E1 (2) < -0.5 then
      raise Program_Error;
   end if;

   -- module 3: array as parameter
   -- ========

   for I in  1 .. N3 loop
      Pa (E1);
   end loop;

   if N3 /= 0 and then E1 (2) < -0.5 then
      raise Program_Error;
   end if;

   -- module 4: conditional jumps
   -- ========

   J2 := 1;

   for I in  1 .. N4 loop
      if J2 = 1 then
         J2 := 2;
      else
         J2 := 3;
      end if;
      if J2 > 2 then
         J2 := 0;
      else
         J2 := 1;
      end if;
      if J2 < 1 then
         J2 := 1;
      else
         J2 := 0;
      end if;
   end loop;

   if N4 /= 0 and then J2 > 1 then
      raise Program_Error;
   end if;

   -- module 5: omitted (in the NPL version 3.1);
   -- ========

   -- module 6: Int arithmetic
   -- ========
   J := 1;
   K := 2;
   L := 3;
   for I in  1 .. N6 loop
      J          := J * (K - J) * (L - K);
      K          := L * K - (L - J) * K;
      L          := (L - K) * (K + J);
      E1 (L - 1) := Float6 (J + K + L);
      E1 (K - 1) := Float6 (J * K * L);
   end loop;

   if N6 /= 0 and then K > 2 then
      raise Program_Error;
   end if;

   -- module 7: trigonometric functions
   -- ========
   X := 0.5;
   Y := 0.5;
   for I in  1 .. N7 loop
      -- +++ tcl 1-8-89 change ATAN to ARCTAN
      X := T *
           Float6 (Arctan
                      (T2 * Sin (X) * Cos (X) /
                       (Cos (X + Y) + Cos (X - Y) - 1.0)));
      Y := T *
           Float6 (Arctan
                      (T2 * Sin (Y) * Cos (Y) /
                       (Cos (X + Y) + Cos (X - Y) - 1.0)));
   end loop;

   if N7 /= 0 and then Y <= -1.0 then
      raise Program_Error;
   end if;

   -- module 8: procedure calls
   -- ========

   X := 1.0;
   Y := 1.0;
   Z := 1.0;
   for I in  1 .. N8 loop
      P3 (X, Y, Z);
   end loop;

   if N8 /= 0 and then Z > 1.0 then
      raise Program_Error;
   end if;

   -- module 9: array references
   -- ========

   J      := 1;
   K      := 2;
   L      := 3;
   E1 (1) := 1.0;
   E1 (2) := 2.0;
   E1 (3) := 3.0;
   for I in  1 .. N9 loop
      P0;
   end loop;

   if N9 /= 0 and then E1 (3) > 3.0 then
      raise Program_Error;
   end if;

   -- module 10: Int arithmetic
   -- =========

   J1 := 2;
   K1 := 3;

   for I in  1 .. N10 loop
      J1 := J1 + K1;
      K1 := K1 + J1;
      J1 := K1 - J1;
      K1 := K1 - J1 - J1;
   end loop;

   if N10 /= 0 and then J1 + K1 /= 5 then
      raise Program_Error;
   end if;

   -- module 11: standard functions
   -- =========

   X := 0.75;
   for I in  1 .. N11 loop
      X := Float6 (Sqrt (Float (Exp (Log (X) / T1))));
      -- +++ tcl 1-8-89 change LN to LOG
   end loop;

   if N11 /= 0 and then (X < 0.75 or X > 1.0) then
      raise Program_Error;
   end if;
   --  <end_measure>

end hl_t_a_02a;
