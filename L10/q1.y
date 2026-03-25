%{
    #include <stdio.h>
    #include <stdlib.h>

    int yylex();
    void yyerror(char *s);
%}

%token TYPE ID SC COMMA NL

%%
start: decl NL { printf("Valid Declaration Statement\n"); exit(0); }
     ;

decl : TYPE list SC
     ;

list : ID
     | list COMMA ID
     ;
%%

void yyerror(char *s) {
    printf("Invalid Declaration Statement\n");
    exit(0);
}

int main() {
    printf("Enter a declaration statement :\n");
    yyparse();
    return 0;
}