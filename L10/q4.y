%{
    #include <stdio.h>
    #include <stdlib.h>

    int yylex();
    int yyerror(char *msg);
%}

%token NUMBER ID NL

%%
input : /* empty */
      | input line
      ;

line  : NL
      | exp NL { printf("Valid Postfix Expression\n"); }
      ;

exp   : NUMBER
      | ID
      | exp exp '+'
      | exp exp '-'
      | exp exp '*'
      | exp exp '/'
      | exp exp '^'
      ;

%%

int yyerror(char *msg) {
    printf("Invalid Expression\n");
    return 0;
}

int main() {
    printf("Enter postfix expression:\n");
    yyparse();
    return 0;
}