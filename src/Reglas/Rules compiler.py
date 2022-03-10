from libs.ply.yacc import yacc
from libs.ply.lex import lex, runmain

File = open("Gramatica libre de contexto.csv")

CODE = ""
output = open("REGLAS.py", "w")

##Example code of a lexxer, just to predefinition test work##
# --- Tokenizer

# All tokens must be named in advance.
tokens = ('STAT', 'DIVISOR', 'COMMA')

# Ignored characters
t_ignore = ' \t'


def t_COMMA(t):
	r'\,'
	global CODE
	CODE += "\n"
	return


def t_DIVISOR(t):
	r'\->'
	global CODE
	CODE += ": "
	return t


def t_STAT(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	global CODE
	CODE += t.value + " "
	return t


def t_jump(t):
	r'\n'
	return


def t_space(t):
	r'\t'
	return


line_number = 0
for line in File:
	lexer = lex()
	lexer.input(line)
	token_list = []

	CODE += "\ndef p_REGLA_" + str(line_number) + "(p):\n"
	CODE += "   '''\n   "
	for tok in lexer:
		token_list.append(tok)
	CODE += "\n   '''\n"
	CODE += "   p[0] =("
	for a in range(1, len(token_list)-1):
		if (a != len(token_list) - 2):
			CODE += "p[" + str(a) + "], "
		else:
			CODE += "p[" + str(a) + "] "

	CODE += ")"
	print(token_list)
	line_number += 1

print(CODE)
output.write(CODE)
File.close()
output.close()
