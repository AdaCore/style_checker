procedure All_Source_Text is
beGin
   Some_Code;

   --  Both branches of the #if have a style violation (extra space before
   --  semicolon) that must be reported.

#if Some_Condition then
   Do_Something ;
#else
   Do_Something_else ;
#end if;

   Some_More_Code;
end All_Source_Text;
