%{
#include "q2.tab.h"
#include <string.h>
%}

%%
"if"                    { return IF; }
"else"                  { return ELSE; }
[0-9]+                  { return NUM; }
[a-zA-Z][a-zA-Z0-9]* { return ID; }
"<="|">="|"=="|"!="|"<"|">" { return RELOP; }
"+="|"-="|"*="|"/="|"="   { return ASSIGN; }
[ \t\n]                 { ; }
.                       { return yytext[0]; }
%%

int yywrap() {
    return 1;
}