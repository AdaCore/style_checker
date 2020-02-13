--  An Ada source file which is supposed to be Ada95 only, but has
--  some Ada 2005 code in it.
procedure Has_05 is
begin
   --  Introduce a deliberate Ada 2005 construct to verify that
   --  the style_checker uses -gnat05, and that the compiler
   --  therefore flags this as a violation.
   raise Constraint_Error with "Bad Message";
end Has_05;
