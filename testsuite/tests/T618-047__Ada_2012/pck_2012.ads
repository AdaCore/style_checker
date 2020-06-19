------------------------------------------------------------------------------
--                    Copyright (C) 2003-2006, AdaCore                      --

package P is
   type Point is tagged
      record
         X, Y : Float := 0.0;
      end record;
   function Is_At_Origin (P : Point) return Boolean is
      (P.X = 0.0 and P.Y = 0.0)
         with Inline;
end P;
