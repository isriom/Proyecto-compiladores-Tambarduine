# from ply.yacc import yacc
# from ply.lex import lex, LexToken
# from ply.lex import TOKEN
from libs.ply.yacc import yacc
from libs.ply.lex import lex, LexToken
from libs.ply.lex import TOKEN

# LETRAS para hits y print !!!

keywords = (
	'SET', 'IF', 'ELSE', 'FOR', 'TO', 'STEP', 'TYPE', 'ENCASO', 'CUANDO', 'ENTONS', 'SINO', 'DEF', 'EXEC', 'PRINCIPAL'
)
booleanOps = (
	'NEG', 'T', 'F', 'TRUE', 'FALSE'
)
hits = (
	'ABANICO', 'VERTICAL', 'PERCUTOR', 'GOLPE', 'VIBRATO', 'METRONOMO'
)
letters = (
	'AB', 'DI', 'A', 'B', 'D', 'I'
)

# List of token names.   This is always required
tokens = (
	         'KEYWORD', 'LETTERS', 'NAME', 'TEXT', 'BOOLEANOP', 'BOOLEAN', 'HIT', 'PRINT', 'FINCASO', 'ID',
	         'ID2', 'VAR', 'DOT', 'LESSEQUAL', 'GREATEEQUAL', 'LESS', 'GREAT', 'EQUALEQUAL', 'EQUAL', 'DIFFERENT',
	         'NUMBER', 'PLUS', 'MINUS', 'POWER', 'TIMES', 'INTDIVIDE', 'DIVIDE', 'MODULUS',
	         'LSCOPE', 'RSCOPE', 'QUOTES', 'LPAREN', 'RPAREN', 'COMMA',
	         'ENDLINE') + keywords + booleanOps + hits + letters

# Regular expression rules for simple tokens
t_LSCOPE = r'\{'
t_RSCOPE = r'\}'
t_QUOTES = r'"'
t_PLUS = r'\+'
t_MINUS = r'-'
t_POWER = r'\*\*'
t_TIMES = r'\*'
t_INTDIVIDE = r'//'
t_DIVIDE = r'/'
t_MODULUS = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_ENDLINE = r'\;'
t_LESSEQUAL = r'<='
t_GREATEEQUAL = r'>='
t_LESS = r'<'
t_GREAT = r'>'
t_EQUALEQUAL = r'=='
t_EQUAL = r'='
t_DIFFERENT = r'!='


###################################### NEWLINE
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)


###################################### IGNORES
t_ignore = ' \t'

t_ignore_COMMENT = r'\#.*'


###################################### ERROR
def t_error(t):
	global lexer

	lexer.error += '\n' + "Illegal character " + str(t.value[0]) + 'in line ' + str(t.lineno)
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)


###################################### TOKENS

def t_bralce(t):
	r'\.'
	t.type = 'DOT'  # Set token type to the expected literal
	return t


def t_BOOLEAN(t):
	r'(True|False)'
	t.value = str(t.value)
	return t


def t_PRINT(t):
	r'println!'
	t.type = 'PRINT'
	t.value = str(t.value)
	return t


def t_FINCASO(t):
	r'Fin-EnCaso'
	t.type = 'FINCASO'
	t.value = str(t.value)
	return t


'''
def t_ID2(t):
    r'.[a-zA-Z_]+'
    if t.value in booleanOps:
        t.type = 'BOOLEANOP'
        return t
    else:
        t_error(t)
'''


def t_ID(t):
	r'[a-zA-Z_]+'
	if t.value.upper() in keywords:
		if t.value == 'Principal':
			print('holi')
		t.type = t.value.upper()
		return t
	elif t.value.upper() in booleanOps:
		t.type = t.value.upper()
		return t
	elif t.value.upper() in hits:
		t.type = t.value.upper()
		return t
	elif t.value.upper() in letters:
		t.type = t.value.upper()
		return t
	else:
		t.type = 'TEXT'
		t.value = str(t.value)
		return t


def t_NUMBER(t):
	r'[0-9]+'
	t.value = int(t.value)
	return t


def t_VAR(t):
	r'@([a-zA-Z_0-9]|_|\?){3,10}'
	t.value = str(t.value)
	return t


# Build the lexer
lexer = lex()
lexer.error = ''

data = '''>= <= = ==> ,{ Def Principal SET println! If "textoprueba. @Aqqaae @var26_? type() < .Neg Abanico() ; //% ** 10 -20 AB *2\n True False Fin-EnCaso'''
# data = '''3 + 5 * 10 - 20 '''
# data = 'a = 3'
# data = '1 + 5\nabce\n77\nif yo'

# Give the lexer some input
# lexer.input(data)

# Tokenize
# for tok in lexer:
# 	# print(tok)
# 	print("Class:" + tok.type + " Value:" + str(tok.value) + " Line:" + str(tok.lineno) + " Pos:" + str(tok.lexpos))
#

#

def GetLexer():
	return lexer
