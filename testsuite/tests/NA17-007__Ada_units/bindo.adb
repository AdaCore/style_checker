------------------------------------------------------------------------------
--                                                                          --
--                         GNAT COMPILER COMPONENTS                         --
--                                                                          --
--                                B I N D O                                 --
--                                                                          --
--                                 B o d y                                  --
--                                                                          --
--             Copyright (C) 2019-2020, Free Software Foundation, Inc.      --

procedure Bindo is
begin
   raise Constraint_Error with "My message";
end Bindo;
