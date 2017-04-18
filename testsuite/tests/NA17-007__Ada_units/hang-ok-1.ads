------------------------------------------------------------------------------
--                                                                          --
--                             ATRE COMPONENTS                              --
--                                                                          --
--                  A T R E . A S I S _ U T I L I T I E S                   --
--                                                                          --
--                                 S p e c                                  --
--                                                                          --
--                     Copyright (C) 2006, AdaCore                          --
--                                                                          --
-- ATRE is free software;  you can redistribute it  and/or  modify it under --
-- terms of the  GNU General Public License as published  by the Free Soft- --
-- ware  Foundation;  either version 2,  or (at your option) any later ver- --
-- sion.  ATRE  is  distributed  in  the hope that it will be  useful,  but --
-- WITHOUT ANY WARRANTY; without even the implied warranty of  MERCHANTABI- --
-- LITY or  FITNESS  FOR A  PARTICULAR  PURPOSE. See the GNU General Public --
-- License  for more details. You  should  have  received a copy of the GNU --
-- General Public License  distributed with GNAT; see file COPYING. If not, --
-- write  to  the Free  Software  Foundation,  59 Temple Place - Suite 330, --
-- Boston,                                                                  --
--                                                                          --
-- ATRE is maintained by ACT Europe (http://www.act-europe.fr).             --
--                                                                          --
------------------------------------------------------------------------------

--  This package contains various ASIS-based routines for ATRE

with GNAT.OS_Lib; use GNAT.OS_Lib;
with Asis;        use Asis;
with Asis.Data_Decomposition;

with ATRE.Common; use ATRE.Common;

package ATRE.Asis_Utilities is

   function Detect_Type_Class
     (RC   : Asis.Data_Decomposition.Record_Component;
      Size : ASIS_Natural)
      return Type_Classes;
   --  Detects the type class for the component. Returns Unknown in case if
   --  in is impossible to define a specific class because of any reason.

   procedure Detect_Component_Range
     (RC          :     Asis.Data_Decomposition.Record_Component;
      RC_Type     :     Type_Classes;
      Component_L : out String_Access;
      Component_R : out String_Access;
      Success     : out Boolean);
   --  Tries to compute the component ranges according to the component
   --  definition (but not to the component base type). If this is possible,
   --  sets Success ON and Component_L and Component_R are set to the (string
   --  images of the left and right bounds of the component range. Otherwise
   --  Success is set OFF, and Component_L and Component_R are undefined.

end ATRE.Asis_Utilities;
