from libs.ply.yacc import yacc
from libs.ply.lex import lex, LexToken
from src.Reglas.REGLAS import *

##Example code of a lexxer, just to predefinition test work##
# --- Tokenizer

# All tokens must be named in advance.
Keywords = (
	'IF', 'ELSE', 'TRUE', 'FALSE', 'sc', 'FOR', 'TO', 'STEP', 'INCASE', 'ENDINCASE', 'DEF', 'PRINCIPAL', 'LP', 'RP',
	'EXEC', 'PRINT', 'METRONOME', 'A', 'COMMA', 'D', 'SET', 'DOT', 'NEG', 'T', 'F', 'B', 'VERTICAL', 'ABANICO', 'I',
	'PERCUTOR', 'DI', 'GOLPE', 'WHEN', 'THEN', 'WHENELSE', 'AB', 'VRIBATO', 'TEXT', 'LESSEQUAL', 'GREATEEQUAL',
	'DIFFERENT', 'NUM')
tokens = Keywords + ('PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
                     'NAME', 'NUMBER', 'POWER', 'LESS', 'GREAT', 'EQUAL', 'EEQUAL', 'LB', 'RB')

# Ignored characters
t_ignore = ' \t'

# Token matching rules are written as regexs
t_PLUS = r'\+'
t_MINUS = r'-'
t_POWER = r'\*\*'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_RB = r'\}'
t_LB = r'\{'
t_LESS = r'\<'
t_GREAT = r'\>'
t_EEQUAL = r'\=='
t_EQUAL = r'\='
t_IF = r'if'
t_ELSE = r'else'
t_TRUE = r'True'
t_FALSE = r'False'
t_NAME = r'\@[a-zA-Z_][a-zA-Z0-9_]*'
t_sc = r'\;'


# A function can be used if there is an associated action.
# Write the matching regex in the docstring.
def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t


# Ignored token with an action associated with it
def t_ignore_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count('\n')


# Error handler for illegal characters
def t_error(t):
	print(f'Illegal character {t.value[0]!r}')
	t.lexer.skip(1)


# Build the lexer object
lexer = lex()

'''Start of Parser'''
precedence = (
	('left', 'NUMBER'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE'),
	('left', 'POWER'),
	('left', 'IF'),
	('left', 'ELSE'),
	('left', 'LB')
)

start='Code'
def p_Code(p):
	'''
	Code : instruction
	'''
	p[0] = (p[1])


# def p_code(p):
# 	'''
# 	code : expression
# 		| ifexpression
# 		| ifelseexpression
# 		| scope
# 	'''
# 	p[0] = ("Code", p[1])


def p_expression(p):
	'''
	expression  : term PLUS term
				| term MINUS term
				| expression MINUS expression
				| expression PLUS expression
	'''
	p[0] = ('binop', p[2], p[1], p[3])


def p_expression_term(p):
	'''
	expression : term
	'''
	p[0] = p[1]


def p_factor_pow(p):
	'''
	factor : factor POWER factor
	'''
	p[0] = ('binop', p[2], p[1], p[3])


def p_term(p):
	'''
	factor : factor TIMES factor
		   | factor DIVIDE factor
	'''
	p[0] = ('binop', p[2], p[1], p[3])


def p_term_factor(p):
	'''
	term : factor
	'''
	p[0] = p[1]


def p_factor_number(p):
	'''
	factor : NUMBER
	'''
	p[0] = ('number', p[1])


def p_factor_name(p):
	'''
	factor : NAME
	'''
	p[0] = ('name', p[1])


def p_factor_unary(p):
	'''
	factor : PLUS factor
		   | MINUS factor
	'''
	p[0] = ('unary', p[1], p[2])


def p_factor_grouped(p):
	'''
	factor : LPAREN expression RPAREN
	'''
	p[0] = ('grouped', p[2])


def p_term_grouped(p):
	'''
	term : LPAREN expression RPAREN
	'''
	p[0] = ('grouped', p[2])


def p_bool_grouped(p):
	'''
	bool : LPAREN bool RPAREN
	'''
	p[0] = ('grouped', p[2])


##From PLY github; https://github.com/dabeaz/ply, Autor David beazley##

def p_less(p):
	'''
	bool : expression LESS expression
		 | factor LESS factor
		 | NUMBER LESS NUMBER
	'''
	p[0] = ('less', p[2], p[1], p[3])


def p_more(p):
	'''
	bool : expression GREAT expression
		 | factor GREAT factor
		 | NUMBER GREAT NUMBER
	'''
	p[0] = ('more', p[2], p[1], p[3])

#
# def p_if(p):
# 	'''
# 	ifexpression : IF bool scope
# 	'''
# 	p[0] = ('ifexpression', p[1], p[2], p[3])
#
#
# def p_else(p):
# 	'''
# 	elseexpression : ELSE scope
# 	'''
# 	p[0] = ('elseexpression', p[1], p[2])
#
#
# def p_if_else(p):
# 	'''
# 	ifelseexpression : ifexpression elseexpression
# 	'''
# 	p[0] = ('ifelseexpression', p[1], p[2])
#
#
# def p_bool_true(p):
# 	'''
# 	bool : TRUE
# 	'''
# 	p[0] = ('bool', p[1])
#
#
# def p_bool_false(p):
# 	'''
# 	bool : FALSE
# 	'''
# 	p[0] = ('bool', p[1])
#
#
# def p_variable(p):
# 	'''
# 	var : NAME EQUAL expression
# 	'''
# 	p[0] = ('var', p[1], p[3])
#
#
# def p_statement(p):
# 	'''
# 	statement : bool
# 	'''
# 	p[0] = ('statement', p[1])
#
#
# def p_scope(p):
# 	'''
# 	scope : LB expression RB
# 		 | LB statement RB
# 	'''
# 	p[0] = ('scope', p[2])
def p_REGLA_A(p):
	'''
	printstatement : bool
	'''
	p[0]=('bool',p[1])

def p_error(p):
	print(f'Syntax error at {p.value!r}')


# Build the parser
parser = yacc()

# Parse an expression
ast = parser.parse('if True {5<5;} else {15<6;};', debug=True)
print(ast)
