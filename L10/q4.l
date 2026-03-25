%{
    #include "q4.tab.h"
%}

%%
[0-9]+          { return NUMBER; }
[a-zA-Z]        { return ID; }
\n              { return NL; }
[ \t]           { ; }
"+"|"-"|"*"|"/"|"^" { return yytext[0]; }
.               { return yytext[0]; }
%%

int yywrap() {
    return 1;
}