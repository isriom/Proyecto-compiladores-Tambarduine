from libs.ply.yacc import yacc
from src.Lexxer.Lex import *
from src.Reglas.REGLAS import *

'''Start of Parser'''
precedence = (
	('left', 'NUMBER'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE', 'INTDIVIDE', 'MODULUS'),
	('left', 'POWER'),
	('left', 'LPAREN', 'RPAREN'),
)

start = "Code"

CODE = ""


def p_REGLA_0(p):
	'''
	Code : instruction
	'''
	p[0] = (p[1])


def p_error(p):
	print(f'Syntax error at {p.value!r}')


# Build the parser
parser = yacc()


# ast = parser.parse('if True {SET @xyz,5;} else {SET @xyz,5;};', debug=True)
# print(ast)
def GetParser():
	return parser


def restartParse():
	pass


def GetCode():
	return CODE
