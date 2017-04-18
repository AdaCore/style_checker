------------------------------------------------------------------------------
--                                                                          --
--             ASIS Tester And iNTerpreter (ASIStant) COMPONENTS            --
--                                                                          --
--                     A S I S T A N T . F U N C E N U M                    --
--                                                                          --
--                                 S p e c                                  --
--                                                                          --
--          Copyright (c) 1997-2006, Free Software Foundation, Inc.         --
--                                                                          --
-- ASIStant is free software; you can redistribute it and/or modify it      --
-- under terms of the  GNU General Public License  as published by the Free --
-- Software Foundation;  either version 2,  or  (at your option)  any later --
-- version. ASIStant is distributed  in the hope  that it will be useful,   --
-- but WITHOUT ANY WARRANTY; without even the implied warranty of MER-      --
-- CHANTABILITY or  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General  --
-- Public License for more details. You should have received a copy of the  --
-- GNU General Public License distributed with GNAT; see file COPYING. If   --
-- not, write to the Free Software Foundation, 59 Temple Place Suite 330,   --
-- Boston, MA 02111-1307, USA.                                              --
--                                                                          --
-- ASIStant is an evolution of ASIStint tool that was created by            --
-- Vasiliy Fofanov as part of a collaboration between Software Engineering  --
-- Laboratory of the Swiss Federal Institute of Technology in Lausanne,     --
-- Switzerland, and the Scientific Research Computer Center of the Moscow   --
-- University, Russia, supported by the Swiss National Science Foundation   --
-- grant #7SUPJ048247, "Development of ASIS for GNAT with industry quality" --
--                                                                          --
-- ASIStant is distributed as a part of the ASIS implementation for GNAT    --
-- (ASIS-for-GNAT) and is maintained by Ada Core Technologies Inc           --
-- (http://www.gnat.com).                                                   --
------------------------------------------------------------------------------

with ASIStant.Table; use ASIStant.Table;

package ASIStant.FuncEnum is

------------------------------------------------------------------------------
--  ASIS queries enumeration and template information
------------------------------------------------------------------------------

------------------------------------------------------------------------------
--    All ASIS 95 queries must be supported, except a generic query
--    Traverse_Element. Failure to recognize any query which is not in the
--    Open Problems List is a bug, and the corresponding bug report will
--    be greatly appreciated.
------------------------------------------------------------------------------

------------------------------------------------------------------------------
--    OPEN PROBLEMS LIST (not implemented queries)
--      Traverse_Element not supported due to major conceptual limitations
--      Asis.Implementation.Set_Status
--      package Asis.Ada_Environments.Containers (all queries & types)
--      Asis.Compilation_Units.Enclosing_Container
--      package Asis.Compilation_Units.Times
--      package Asis.Ids
--      package Asis.Data_Decomposition and <...>.Portable_Transfer
------------------------------------------------------------------------------

------------------------------------------------------------------------------
--    For brevity sake, the following convention is used to identify a query
--    profile: the types of query parameters are written one after another in
--    an abbreviated form, then the portion Ret<Return Type Abbreviation> is
--    appended. Below is a list of abbreviations:
--        Bool        - Boolean
--        Ctx         - Asis.Context
--        CUnit       - Asis.Compilation_Unit
--        CUnitList   - Asis.Compilation_Unit_List
--        DDA_ArrC     - DDA.Array_Component
--        DDA_ArrCList - DDA.Array_Component_List
--        DDA_RecC     - DDA.Record_Component
--        DDA_RecCList - DDA.Record_Component_List
--        Elem        - Asis.Element
--        ElemList    - Asis.Element_List
--        Int         - Integer/Asis.Asis_Integer
--        Line        - Asis.Text.Line
--        LineList    - Asis.Text.Line_List
--        Null        - (RetNull) Procedure
--        Relship     - Asis.Compilation_Units.Relationship
--        Span        - Asis.Text.Span
--
--    FOR EXAMPLE, the profile
--        (C : Asis.Compilation_Unit; I : Integer) return Asis.Element_List
--    will be represented as
--        CUnitIntRetElemList
------------------------------------------------------------------------------

--  Enumeration of all queries
   type Switch_Index is (
   --  Placeholder
      Invalid_Index,
   --  CtxRetBool
      Exists,
      Is_Open,
      Has_Associations,
   --  CtxRetCUnitList
      Compilation_Unit_Bodies,
      Compilation_Units,
      Library_Unit_Declarations,
   --  CtxRetElemList
      Configuration_Pragmas,
   --  CtxRetNull
      Close,
      Dissociate,
      Open,
   --  CtxRetString
      Debug_Image_Ctx,
      Name,
      Parameters,
   --  CtxStringStringRetNull
      Associate,
   --  CUnitBoolRetElemList
      Context_Clause_Elements,
   --  CUnitCtxRetCUnit
      Corresponding_Body_CU_Ctx,
      Corresponding_Declaration_CU_Ctx,
   Corresponding_Parent_Declaration_Ctx,
   Corresponding_Subunit_Parent_Body_Ctx,
   --  CUnitCtxRetCUnitList
      Corresponding_Children_Ctx,
      Subunits_Ctx,
   --  CUnitCUnitRetBool
      Is_Equal_CU,
      Is_Identical_CU,
   --  CUnitIntIntRetElem
      Find_Element,
   --  CUnitListCtxRetRelship
      Elaboration_Order,
   --  CUnitListCUnitListCtxStringRetRelship
      Semantic_Dependence_Order,
   --  CUnitListRetBool
      Is_Nil_CUL,
   --  CUnitRetBool
      Can_Be_Main_Program,
      Exists_CU,
      Is_Body_Required,
      Is_Nil_CU,
   --  CUnitRetCtx
      Enclosing_Context,
   --  CUnitRetCUnit
      Corresponding_Body_CU,
      Corresponding_Declaration_CU,
      Corresponding_Parent_Declaration,
      Corresponding_Subunit_Parent_Body,
   --  CUnitRetCUnitList
      Corresponding_Children,
      Subunits,
   --  CUnitRetElem
      Browse_CU,
      Unit_Declaration,
   --  CUnitRetElemList
      Compilation_Pragmas,
   --  CUnitRetString
      Compilation_Command_Line_Options,
      Debug_Image_CU,
      Object_Form,
      Object_Name,
      Text_Form,
      Text_Name,
      Unit_Class,
      Unit_Full_Name,
      Unit_Kind,
      Unit_Origin,
      Unique_Name,
   --  CUnitStringRetATime
      Attribute_Time,
   --  CUnitStringRetBool
      Has_Attribute,
   --  CUnitStringRetString
      Attribute_Values,
   --  DDA_ArrCRetDDA_ArrC
      DDA_Array_Components_2,
   --  DDA_ArrCRetDDA_RecCList
      DDA_Discriminant_Components_2,
      DDA_Record_Components_2,
   --  DDA_ArrCRetElem
      DDA_Component_Indication,
   --  DDA_RecCRetDDA_ArrC
      DDA_Array_Components_1,
   --  DDA_RecCRetDDA_RecCList
      DDA_Discriminant_Components_1,
      DDA_Record_Components_1,
   --  DDA_RecCRetElem
      DDA_Component_Declaration,
   --  ElemBoolRetElemList
      Accept_Body_Exception_Handlers,
      Accept_Body_Statements,
      Block_Declarative_Items,
      Block_Exception_Handlers,
      Block_Statements,
      Body_Declarative_Items,
      Body_Exception_Handlers,
      Body_Statements,
      Call_Statement_Parameters,
      Component_Clauses,
      Discriminant_Associations,
      Extended_Return_Exception_Handlers,  --  ASIS 2005
      Extended_Return_Statements,  --  ASIS 2005
      Function_Call_Parameters,
      Generic_Actual_Part,
      Generic_Formal_Part,
      Handler_Statements,
      Loop_Statements,
      Private_Part_Declarative_Items,
      Private_Part_Items,
      Protected_Operation_Items,
      Record_Component_Associations,
      Record_Components,
      Sequence_Of_Statements,
      Statement_Paths,
      Variants,
      Visible_Part_Declarative_Items,
      Visible_Part_Items,
   --  ElemCtxRetElem
      Corresponding_Body_Ctx,
      Corresponding_Body_Stub_Ctx,
      Corresponding_Declaration_Ctx,
      Corresponding_Subunit_Ctx,
      Corresponding_Type_Declaration_Ctx,
   --  ElemElemBoolRetBool
      Is_Referenced,
   --  ElemElemBoolRetElemList
      References,
   --  ElemElemRetBool
      Is_Equal,
      Is_Identical,
   --  ElemElemRetElem
      Enclosing_Element_EEE,
   --  ElemIntIntRetLineList
      Lines_2,
   --  ElemListRetBool
      Is_Nil_EL,
   --  ElemRetBool
      Declarations_Is_Private_Present,
      Definitions_Is_Private_Present,
      Is_Declare_Block,
      Is_Defaulted_Association,
      Declarations_Is_Name_Repeated,
      Statements_Is_Name_Repeated,
      Is_Nil,
      Is_Not_Null_Return,  --  ASIS 2005
      Is_Not_Overriding_Declaration,  --  ASIS 2005
      Is_Normalized,
      Is_Overriding_Declaration,  --  ASIS 2005
      Is_Part_Of_Implicit,
      Is_Part_Of_Inherited,
      Is_Part_Of_Instance,
      Is_Prefix_Call,
      Is_Prefix_Notation,  --  ASIS 2005
      Is_Private_Present,
      Is_Subunit,
      Is_Text_Available,
   --  ElemRetCUnit
      Enclosing_Compilation_Unit,
   --  ElemRetDDA_ArrC
      DDA_Array_Components,
   --  ElemRetDDA_RecCList
      DDA_Discriminant_Components,
      DDA_Record_Components,
   --  ElemRetElem
      Accept_Entry_Direct_Name,
      Accept_Entry_Index,
      Access_To_Function_Result_Profile,
      Access_To_Object_Definition,
      Actual_Parameter,
      Allocator_Qualified_Expression,
      Allocator_Subtype_Indication,
      Ancestor_Subtype_Indication,
      Anonymous_Access_To_Object_Subtype_Mark,  -- ASIS 2005
      Array_Component_Definition,
      Assignment_Expression,
      Assignment_Variable_Name,
      Associated_Message,  --  ASIS 2005
      Attribute_Designator_Identifier,
      Body_Block_Statement,
      Browse,
      Called_Name,
      Case_Expression,
      Choice_Parameter_Specification,
      Component_Clause_Position,
      Component_Clause_Range,
      Component_Definition_View,  --  ASIS 2005
      Component_Expression,
      Component_Subtype_Indication,
      Condition_Expression,
      Converted_Or_Qualified_Expression,
      Converted_Or_Qualified_Subtype_Mark,
      Corresponding_Base_Entity,
      Corresponding_Body,
      Corresponding_Body_Stub,
      Corresponding_Called_Entity,
      Corresponding_Called_Function,
      Corresponding_Constant_Declaration,
      Corresponding_Declaration,
      Corresponding_Destination_Statement,
      Corresponding_Entry,
      Corresponding_Equality_Operator,
      Corresponding_Expression_Type,
      Corresponding_Expression_Type_Definition,  --  ASIS 2005
      Corresponding_First_Subtype,
      Corresponding_Generic_Element,
      Corresponding_Last_Constraint,
      Corresponding_Last_Subtype,
      Corresponding_Loop_Exited,
      Corresponding_Name_Declaration,
      Corresponding_Name_Definition,
      Corresponding_Parent_Subtype,
      Corresponding_Root_Type,
      Corresponding_Subprogram_Derivation,
      Corresponding_Subunit,
      Corresponding_Type,
      Corresponding_Type_Declaration,
      Corresponding_Type_Structure,
      Declaration_Subtype_Mark,
      Defining_Prefix,
      Defining_Selector,
      Delay_Expression,
      Delta_Expression,
      Digits_Expression,
      Discriminant_Direct_Name,
      Discriminant_Expression,
      Discriminant_Part,
      Enclosing_Element,
      Entry_Barrier,
      Entry_Family_Definition,
      Entry_Index_Specification,
      Exit_Condition,
      Exit_Loop_Name,
      Expression_Parenthesized,
      Extension_Aggregate_Expression,
      For_Loop_Parameter_Specification,
      Formal_Parameter,
      Formal_Subprogram_Default,
      Generic_Unit_Name,
      Goto_Label,
      Guard,
      Initialization_Expression,
      Integer_Constraint,
      Lower_Bound,
      Membership_Test_Expression,
      Membership_Test_Range,
      Membership_Test_Subtype_Mark,
      Mod_Clause_Expression,
      Mod_Static_Expression,
      Object_Declaration_View,
      Parent_Subtype_Indication,
      Prefix,
      Qualified_Expression,
      Raised_Exception,
      Range_Attribute,
      Real_Range_Constraint,
      Record_Definition,
      Renamed_Entity,
      Representation_Clause_Expression,
      Representation_Clause_Name,
      Requeue_Entry_Name,
      Result_Profile,
      Return_Expression,
      Return_Object_Declaration,  --  ASIS 2005
      Selector,
      Short_Circuit_Operation_Left_Expression,
      Short_Circuit_Operation_Right_Expression,
      Slice_Range,
      Specification_Subtype_Definition,
      Statement_Identifier,
      Subtype_Constraint,
      Subtype_Mark,
      Type_Declaration_View,
      Upper_Bound,
      While_Condition,
   --  ElemRetElemList
      Aborted_Tasks,
      Accept_Parameters,
      Access_To_Subprogram_Parameter_Profile,
      Array_Component_Associations,
      Array_Component_Choices,
      Attribute_Designator_Expressions,
      Case_Statement_Alternative_Choices,
      Clause_Names,
      Corresponding_Name_Definition_List,
      Corresponding_Pragmas,
      Corresponding_Representation_Clauses,
      Corresponding_Type_Operators,
      DDA_All_Named_Components,
      Declaration_Interface_List,  --  ASIS 2005
      Definition_Interface_List,  --  ASIS 2005
      Discrete_Ranges,
      Discrete_Subtype_Definitions,
      Discriminant_Selector_Names,
      Discriminants,
      Enumeration_Literal_Declarations,
      Exception_Choices,
      Implicit_Components,
      Implicit_Inherited_Declarations,
      Implicit_Inherited_Subprograms,
      Index_Expressions,
      Index_Subtype_Definitions,
      Label_Names,
      Names,
      Parameter_Profile,
      Pragma_Argument_Associations,
      Pragmas,
      Record_Component_Choices,
      Variant_Choices,
   --  ElemRetInt
      First_Line_Number,
      Hash,
      Last_Line_Number,
   --  ElemRetLineList
      Lines,
   --  ElemRetSpan
      Compilation_Span,
      Compilation_Unit_Span,
      Element_Span,
   --  ElemRetString (mainly additional queries to cover enum results)
      Access_Type_Kind,
      Association_Kind,
      Attribute_Kind,
      Clause_Kind,
      Constraint_Kind,
      Debug_Image,
      Declaration_Kind,
      Declaration_Origin,
      Default_Kind,
      Defining_Name_Image,
      Defining_Name_Kind,
      Definition_Kind,
      Discrete_Range_Kind,
      Element_Image,
      Element_Kind,
      Expression_Kind,
      Formal_Type_Kind,
      Interface_Kind,  --  ASIS 2005
      Mode_Kind,
      Name_Image,
      Operator_Kind,
      Path_Kind,
      Position_Number_Image,
      Pragma_Kind,
      Pragma_Name_Image,
      Representation_Clause_Kind,
      Representation_Value_Image,
      Root_Type_Kind,
      Statement_Kind,
      Trait_Kind,
      Type_Kind,
      Value_Image,
   --  ElemSpanRetLineList
      Lines_1,
   --  IntIntRetBool
      Eq,
      Gt,
      Lt,
   --  IntIntRetInt
      Add,
      Sub,
   --  LineRetString
      Comment_Image,
      Debug_Image_L,
      Line_Image,
      Non_Comment_Image,
   --  RelshipRetCUnitList
      Consistent,
      Inconsistent,
      Missing,
      Circular,
   --  RetBool
      Attributes_Are_Supported,
      Default_In_Mode_Supported,
      Discriminant_Associations_Normalized,
      Function_Call_Parameters_Normalized,
      Generic_Actual_Part_Normalized,
      Generic_Macro_Expansion_Supported,
      Implicit_Components_Supported,
      Inherited_Declarations_Supported,
      Inherited_Subprograms_Supported,
      Is_Commentary_Supported,
      Is_Finalized,
      Is_Formal_Parameter_Named_Notation_Supported,
      Is_Initialized,
      Is_Line_Number_Supported,
      Is_Prefix_Call_Supported,
      Is_Span_Column_Position_Supported,
      Object_Declarations_Normalized,
      Predefined_Operations_Supported,
      Record_Component_Associations_Normalized,
   --  RetCUnit
      Nil_Compilation_Unit,
   --  RetCUnitList
      Nil_Compilation_Unit_List,
   --  RetElem
      Nil_Element,
   --  RetElemList
      Nil_Element_List,
   --  RetLine
      Nil_Line,
   --  RetRelship
      Nil_Relationship,
   --  RetSpan
      Nil_Span,
   --  RetString
      Asis_Implementor,
      Asis_Implementor_Information,
      Asis_Implementor_Version,
      Asis_Version,
      Attribute_Value_Delimiter,
      Default_Name,
      Default_Parameters,
      Delimiter_Image,
   Diagnosis,
   Status,
   --  SpanRetBool
      Is_Nil_Sp,
   --  SpanRetInt
      First_Column,
      First_Line,
      Last_Column,
      Last_Line,
   --  StringCtxRetCUnit
      Compilation_Unit_Body,
      Library_Unit_Declaration,
   --  StringRetNull
      Finalize,
      Initialize,
   --  StringStringRetBool
      Eq_SS,
      Gt_SS,
      Lt_SS,
   --  StringStringRetString
      Concat
   );

   subtype Func_Param is Var_Type;

   type Profile_Range is new Integer range 0 .. 4;

   type Func_Syntax is array (Profile_Range) of Func_Param;
   --  0 is the type of return value, 1..4 - of params 1..4

   type Switch_Node is record
      From, To : Switch_Index;
      SelectID : Positive;
      Synt     : Func_Syntax;
   end record;

   SI_LENGTH : constant Natural := 68;

   Switch_Info : array (1 .. SI_LENGTH) of Switch_Node := (
--  CtxRetBool
   (Exists, Has_Associations, 10,
      (Par_Boolean, Par_Context, Par_Absent, Par_Absent, Par_Absent)),
--  CtxRetCUnitList
   (Compilation_Unit_Bodies, Library_Unit_Declarations, 20,
      (Par_CUnitList, Par_Context, Par_Absent, Par_Absent, Par_Absent)),
--  CtxRetElemList
   (Configuration_Pragmas, Configuration_Pragmas, 30,
   (Par_ElemList, Par_Context, Par_Absent, Par_Absent, Par_Absent)),
--  CtxRetNull
   (Close, Open, 40,
      (Par_Absent, Par_Context, Par_Absent, Par_Absent, Par_Absent)),
--  CtxRetString
   (Debug_Image_Ctx, Parameters, 50,
      (Par_String, Par_Context, Par_Absent, Par_Absent, Par_Absent)),
--  CtxStringStringRetNull
   (Associate, Associate, 60,
      (Par_Absent, Par_Context, Par_String, Par_String, Par_Absent)),
--  CUnitBoolRetElemList
   (Context_Clause_Elements, Context_Clause_Elements, 70,
      (Par_ElemList, Par_CUnit, Par_Boolean, Par_Absent, Par_Absent)),
--  CUnitCtxRetCUnit
   (Corresponding_Body_CU_Ctx, Corresponding_Subunit_Parent_Body_Ctx, 80,
      (Par_CUnit, Par_CUnit, Par_Context, Par_Absent, Par_Absent)),
--  CUnitCtxRetCUnitList
   (Corresponding_Children_Ctx, Subunits_Ctx, 90,
      (Par_CUnitList, Par_CUnit, Par_Context, Par_Absent, Par_Absent)),
--  CUnitCUnitRetBool
   (Is_Equal_CU, Is_Identical_CU, 93,
      (Par_Boolean, Par_CUnit, Par_CUnit, Par_Absent, Par_Absent)),
--  CUnitIntIntRetElem
   (Find_Element, Find_Element, 95,
      (Par_Element, Par_CUnit, Par_Integer, Par_Integer, Par_Absent)),
--  CUnitListCtxRetRelship
   (Elaboration_Order, Elaboration_Order, 97,
      (Par_Relationship, Par_CUnitList, Par_Context, Par_Absent, Par_Absent)),
--  CUnitListCUnitListCtxStringRetRelship
   (Semantic_Dependence_Order, Semantic_Dependence_Order, 98,
      (Par_Relationship, Par_CUnitList, Par_CUnitList, Par_Context, Par_String)
   ),
--  CUnitListRetBool
   (Is_Nil_CUL, Is_Nil_CUL, 100,
      (Par_Boolean, Par_CUnitList, Par_Absent, Par_Absent, Par_Absent)),
--  CUnitRetBool
   (Can_Be_Main_Program, Is_Nil_CU, 110,
      (Par_Boolean, Par_CUnit, Par_Absent, Par_Absent, Par_Absent)),
--  CUnitRetCtx
   (Enclosing_Context, Enclosing_Context, 120,
      (Par_Context, Par_CUnit, Par_Absent, Par_Absent, Par_Absent)),
--  CUnitRetCUnit
   (Corresponding_Body_CU,
    Corresponding_Subunit_Parent_Body, 130,
      (Par_CUnit, Par_CUnit, Par_Absent, Par_Absent, Par_Absent)),
--  CUnitRetCUnitList
   (Corresponding_Children, Subunits, 140,
      (Par_CUnitList, Par_CUnit, Par_Absent, Par_Absent, Par_Absent)),
--  CUnitRetElem
   (Browse_CU, Unit_Declaration, 150,
      (Par_Element, Par_CUnit, Par_Absent, Par_Absent, Par_Absent)),
--  CUnitRetElemList
   (Compilation_Pragmas, Compilation_Pragmas, 160,
      (Par_ElemList, Par_CUnit, Par_Absent, Par_Absent, Par_Absent)),
--  CUnitRetString
   (Compilation_Command_Line_Options, Unique_Name, 180,
      (Par_String, Par_CUnit, Par_Absent, Par_Absent, Par_Absent)),
--  CUnitStringRetATime
   (Attribute_Time, Attribute_Time, 190,
      (Par_ATime, Par_CUnit, Par_String, Par_Absent, Par_Absent)),
--  CUnitStringRetBool
   (Has_Attribute, Has_Attribute, 200,
      (Par_Boolean, Par_CUnit, Par_String, Par_Absent, Par_Absent)),
--  CUnitStringRetString
   (Attribute_Values, Attribute_Values, 210,
      (Par_String, Par_CUnit, Par_String, Par_Absent, Par_Absent)),
--  DDA_ArrCRetDDA_ArrC
   (DDA_Array_Components_2, DDA_Array_Components_2, 212,
      (Par_DDA_Array_Component, Par_DDA_Array_Component, Par_Absent,
       Par_Absent, Par_Absent)),
--  DDA_ArrCRetDDA_RecCList
   (DDA_Discriminant_Components_2, DDA_Record_Components_2, 214,
      (Par_DDA_Record_Component_List, Par_DDA_Array_Component, Par_Absent,
       Par_Absent, Par_Absent)),
--  DDA_ArrCRetElem
   (DDA_Component_Indication, DDA_Component_Indication, 216,
      (Par_Element, Par_DDA_Array_Component, Par_Absent, Par_Absent,
       Par_Absent)),
--  DDA_RecCRetDDA_ArrC
   (DDA_Array_Components_1, DDA_Array_Components_1, 217,
      (Par_DDA_Array_Component, Par_DDA_Record_Component, Par_Absent,
       Par_Absent, Par_Absent)),
--  DDA_RecCRetDDA_RecCList
   (DDA_Discriminant_Components_1, DDA_Record_Components_1, 218,
      (Par_DDA_Record_Component_List, Par_DDA_Record_Component, Par_Absent,
       Par_Absent, Par_Absent)),
--  DDA_RecCRetElem
   (DDA_Component_Declaration, DDA_Component_Declaration, 219,
      (Par_Element, Par_DDA_Record_Component, Par_Absent, Par_Absent,
       Par_Absent)),
--  ElemBoolRetElemList
   (Accept_Body_Exception_Handlers, Visible_Part_Items, 220,
      (Par_ElemList, Par_Element, Par_Boolean, Par_Absent, Par_Absent)),
--  ElemCtxRetElem
   (Corresponding_Body, Corresponding_Type_Declaration_Ctx, 230,
      (Par_Element, Par_Element, Par_Context, Par_Absent, Par_Absent)),
--  ElemElemBoolRetBool
   (Is_Referenced, Is_Referenced, 240,
      (Par_Boolean, Par_Element, Par_Element, Par_Boolean, Par_Absent)),
--  ElemElemBoolRetElemList
   (References, References, 250,
      (Par_ElemList, Par_Element, Par_Element, Par_Boolean, Par_Absent)),
--  ElemElemRetBool
   (Is_Equal, Is_Identical, 255,
      (Par_Boolean, Par_Element, Par_Element, Par_Absent, Par_Absent)),
--  ElemElemRetElem
   (Enclosing_Element_EEE, Enclosing_Element_EEE, 260,
      (Par_Element, Par_Element, Par_Element, Par_Absent, Par_Absent)),
--  ElemIntIntRetLineList
   (Lines_2, Lines_2, 265,
      (Par_Line_List, Par_Element, Par_Integer, Par_Integer, Par_Absent)),
--  ElemListRetBool
   (Is_Nil_EL, Is_Nil_EL, 270,
      (Par_Boolean, Par_ElemList, Par_Absent, Par_Absent, Par_Absent)),
--  ElemRetBool
   (Declarations_Is_Private_Present, Is_Text_Available, 280,
      (Par_Boolean, Par_Element, Par_Absent, Par_Absent, Par_Absent)),
--  ElemRetCUnit
   (Enclosing_Compilation_Unit, Enclosing_Compilation_Unit, 290,
      (Par_CUnit, Par_Element, Par_Absent, Par_Absent, Par_Absent)),
--  ElemRetDDA_ArrC
   (DDA_Array_Components, DDA_Array_Components, 293,
      (Par_DDA_Array_Component, Par_Element, Par_Absent, Par_Absent,
       Par_Absent)),
--  ElemRetDDA_RecCList
   (DDA_Discriminant_Components, DDA_Record_Components, 295,
      (Par_DDA_Record_Component_List, Par_Element, Par_Absent, Par_Absent,
       Par_Absent)),
--  ElemRetElem
   (Accept_Entry_Direct_Name, While_Condition, 300,
      (Par_Element, Par_Element, Par_Absent, Par_Absent, Par_Absent)),
--  ElemRetElemList
   (Aborted_Tasks, Variant_Choices, 310,
      (Par_ElemList, Par_Element, Par_Absent, Par_Absent, Par_Absent)),
--  ElemRetInt
   (First_Line_Number, Last_Line_Number, 320,
      (Par_Integer, Par_Element, Par_Absent, Par_Absent, Par_Absent)),
--  ElemRetLineList
   (Lines, Lines, 325,
      (Par_Line_List, Par_Element, Par_Absent, Par_Absent, Par_Absent)),
--  ElemRetSpan
   (Compilation_Span, Element_Span, 330,
      (Par_Span, Par_Element, Par_Absent, Par_Absent, Par_Absent)),
--  ElemRetString
   (Access_Type_Kind, Value_Image, 340,
      (Par_String, Par_Element, Par_Absent, Par_Absent, Par_Absent)),
--  ElemSpanRetLineList
   (Lines_1, Lines_1, 342,
      (Par_Line_List, Par_Element, Par_Span, Par_Absent, Par_Absent)),
--  IntIntRetBool
   (Eq, Lt, 343,
      (Par_Boolean, Par_Integer, Par_Integer, Par_Absent, Par_Absent)),
--  IntIntRetInt
   (Add, Sub, 346,
      (Par_Integer, Par_Integer, Par_Integer, Par_Absent, Par_Absent)),
--  LineRetString
   (Comment_Image, Non_Comment_Image, 347,
      (Par_String, Par_Line, Par_Absent, Par_Absent, Par_Absent)),
--  RelshipRetCUnitList
   (Consistent, Circular, 348,
      (Par_CUnitList, Par_Relationship, Par_Absent, Par_Absent, Par_Absent)),
--  RetBool
   (Attributes_Are_Supported, Record_Component_Associations_Normalized, 350,
      (Par_Boolean, Par_Absent, Par_Absent, Par_Absent, Par_Absent)),
--  RetCUnit
   (Nil_Compilation_Unit, Nil_Compilation_Unit, 360,
      (Par_CUnit, Par_Absent, Par_Absent, Par_Absent, Par_Absent)),
--  RetCUnitList
   (Nil_Compilation_Unit_List, Nil_Compilation_Unit_List, 370,
      (Par_CUnitList, Par_Absent, Par_Absent, Par_Absent, Par_Absent)),
--  RetElem
   (Nil_Element, Nil_Element, 380,
      (Par_Element, Par_Absent, Par_Absent, Par_Absent, Par_Absent)),
--  RetElemList
   (Nil_Element_List, Nil_Element_List, 390,
      (Par_ElemList, Par_Absent, Par_Absent, Par_Absent, Par_Absent)),
--  RetLine
   (Nil_Line, Nil_Line, 400,
      (Par_Line, Par_Absent, Par_Absent, Par_Absent, Par_Absent)),
--  RetRelship
   (Nil_Relationship, Nil_Relationship, 405,
      (Par_Relationship, Par_Absent, Par_Absent, Par_Absent, Par_Absent)),
--  RetSpan
   (Nil_Span, Nil_Span, 410,
      (Par_Span, Par_Absent, Par_Absent, Par_Absent, Par_Absent)),
--  RetString
   (Asis_Implementor, Status, 420,
      (Par_String, Par_Absent, Par_Absent, Par_Absent, Par_Absent)),
--  SpanRetBool
   (Is_Nil_Sp, Is_Nil_Sp, 430,
      (Par_Boolean, Par_Span, Par_Absent, Par_Absent, Par_Absent)),
--  SpanRetInt
   (First_Column, Last_Line, 435,
      (Par_Integer, Par_Span, Par_Absent, Par_Absent, Par_Absent)),
--  StringCtxRetCUnit
   (Compilation_Unit_Body, Library_Unit_Declaration, 440,
      (Par_CUnit, Par_String, Par_Context, Par_Absent, Par_Absent)),
--  StringRetNull
   (Finalize, Initialize, 450,
      (Par_Absent, Par_String, Par_Absent, Par_Absent, Par_Absent)),
--  StringStringRetBool
   (Eq_SS, Lt_SS, 460,
      (Par_Boolean, Par_String, Par_String, Par_Absent, Par_Absent)),
--  StringStringRetString
   (Concat, Concat, 470,
      (Par_String, Par_String, Par_String, Par_Absent, Par_Absent))
);

end ASIStant.FuncEnum;