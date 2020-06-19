------------------------------------------------------------------------------
--                    Copyright (C) 2003-2006, AdaCore                      --

function F2020 (I : Integer) return String
is
   type R is record
      I : Integer;
   end record;
   X : R := (I => I);
   Y : String := X'Image; -- Legal in Ada 2020
begin
   if Y (Y'First) /= Character'Last then
      Y (Y'First) := @'Last;  -- Requires -gnat2020
   end if;
   return Y;
end F2020;
