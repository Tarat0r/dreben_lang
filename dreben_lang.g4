grammar dreben_lang;

program: (stmt)* EOF;

stmt:	varDecl
	| assignment
	| print
	| ifstmt
	| blockstmt
	| whilestmt
        ;
        
expr: 	'(' expr ')'					#parenthesisExpr
	| left=expr op=(ASTERISK | SLASH) right=expr	#mulDivExpr
	| left=expr op=(PLUS | MINUS) right=expr	#plusMinusExpr
	| left=expr compOperator right=expr		#compExpr
	| BOOL						#boolExpr
	| ID						#idExp
	| NUM						#numExpr
	| STRING					#stringExpr
	;

// описания отдельных выражений и утверждений
varDecl: 'Променлива' ID 'равна' expr ';'	;

assignment: ID 'равно' expr ';'	;

compOperator: op=(LESS | LESS_OR_EQUAL | EQUAL | NOT_EQUAL | GREATER | GREATER_OR_EQUAL) ;

print: 'Покажи'  expr  ';'			;

blockstmt: '{' (stmt)* '}' 			;


ifstmt:		'Ако' '„' expr '“' stmt  elsestmt? ;

elsestmt:	'Иначе' stmt 			;

whilestmt:	'Докато' expr stmt	;

// список токенов
// ID		: [a-zA-Z_] [a-zA-Z_0-9]* ;


ASTERISK            : 'по' ; // *
SLASH               : 'делено на' ; // \
PLUS                : 'плюс' ; // +
MINUS               : 'минус' ; // -

ASSIGN              : 'равно' ; //=
EQUAL               : 'е равно на' ; // ==
NOT_EQUAL           : 'НЕ е равно на' ; //!=
LESS                : 'е по-малко от' ; //<
LESS_OR_EQUAL       : 'е по-малко или равно от' ; //<=
GREATER             : 'е по-голямо от' ; //>
GREATER_OR_EQUAL    : 'е по-голямо или равно от' ; //>=

BOOL     : 'Истина' | 'Лъжа';              // Булевы значения
ID      : [a-zA-Zа-яА-Я_] [a-zA-Zа-яА-Я_0-9]* ;
NUM		: [0-9]+ ;
STRING : '"' (~["\\\r\n] | '\\' .)* '"' ;  // Строки

LINE_COMMENT        : '//' ~[\n\r]* -> skip;
COMMENT             : '/*' .*? '*/' -> skip ;
SPACE               : [ \r\n\t]+ -> skip;