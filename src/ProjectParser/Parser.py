from libs.ply.yacc import yacc
from src.Lexxer.Lex import *
from src.Reglas.REGLAS import *

'''Start of Parser'''
precedence = (
	('left', 'SET', 'VAR'),
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
	if p == None:
		print("end of file reached, Parsed finished or most probabily Syntax error at the end of file")
	else:
		previous_token = parser.symstack[-1]
		if type(previous_token) == type(p):
				print("\nSyntax error in  " + str(previous_token) + "in line " + str(parser.symstack[-1].lineno))
		else:
				print("\nSyntax error in  " + str(p) + "in line " + str(p.lineno))



# Build the parser
parser = yacc(debug=True)
parser.error = ''


# ast = parser.parse('if True {SET @xyz,5;} else {SET @xyz,5;};', debug=True)
# print(ast)
def GetParser():
	return parser


def restartParse():
	pass


def GetCode():
	return CODE
