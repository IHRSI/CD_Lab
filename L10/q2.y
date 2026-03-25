%{
    #include <stdio.h>
    #include <stdlib.h>

    int yylex();
    void yyerror(char *s);
%}

%token IF ELSE ID NUM RELOP ASSIGN

%%
start : IF_STMT { printf("Valid Decision Making Statement\n"); exit(0); }
      ;

IF_STMT : IF '(' CONDITION ')' BLOCK
        | IF '(' CONDITION ')' BLOCK ELSE BLOCK
        ;

BLOCK   : STMT ';'
        | '{' STMT_LIST '}'
        ;

STMT_LIST : STMT_LIST STMT ';'
          | STMT ';'
          | /* empty */
          ;

CONDITION : EXPR RELOP EXPR
          | EXPR
          ;

STMT : ID ASSIGN EXPR
     | IF_STMT
     ;

EXPR : ID 
     | NUM
     ;

%%

void yyerror(char *s) {
    printf("Invalid Decision Making Statement\n");
    exit(0);
}

int main() {
    printf("Enter the decision statement:\n");
    yyparse();
    return 0;
}