%{
    #include<stdio.h>
    #include<stdlib.h>

    int yylex();
    int yyerror(char *msg);
    extern FILE *yyin;
%}

%token NUMBER ID NL
%left '+'
%left '-'
%left '*'
%left '/'

%%
stmt : exp NL { printf("Valid Expression\n"); exit(0); }
    ;

exp : exp '+' term
    | exp '-' term
    | term
    ;

term : term '*' factor
     |  term '/' factor
     |factor
     ;

factor : ID
       | NUMBER
       ;
%%

int yyerror(char *msg)
{
    printf("Invalid Expression\n");
    exit(0);
}

int main ()
{
    printf("Enter the expression\n");
    yyparse();
    return 0;
}