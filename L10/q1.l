%{
    #include "q1.tab.h"
%}

%%
"int"|"float"|"char"|"double" { return TYPE; }
[a-zA-Z][a-zA-Z0-0]* { return ID; }
","                           { return COMMA; }
";"                           { return SC; }
"\n"                          { return NL; }
[ \t]                         { ; }
.                             { return yytext[0]; }
%%

int yywrap() {
    return 1;
}