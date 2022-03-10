import ply.lex as lex
import ply.yacc as yacc
from ply.lex import TOKEN


# LETRAS para hits y print !!!

keywords = (
    'SET', 'If', 'Else', 'for', 'to', 'Step', 'type', 'EnCaso', 'Cuando', 'EnTons', 'SiNo', 'Def', 'Exec'
)
booleanOps = (
    'Neg','T','F',
)
hits = (
    'Abanico','Vertical','Percutor','Golpe','Vibrato','Metronomo'
)

literals = [ '.' ]


 # List of token names.   This is always required
tokens = (
    'KEYWORD','BOOLEANOP','BOOLEAN','HIT','PRINT','FINCASO','ID','ID2','VAR',
    'NUMBER','PLUS','MINUS','POWER','TIMES','INTDIVIDE','DIVIDE','MODULUS',
    'LSCOPE','RSCOPE','LPAREN','RPAREN','COMMA','ENDLINE') + keywords + booleanOps + hits
 
 # Regular expression rules for simple tokens
t_LSCOPE  = r'\{'
t_RSCOPE  = r'\}'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_POWER   = r'\*\*'
t_TIMES   = r'\*'
t_INTDIVIDE = r'//'
t_DIVIDE  = r'/'
t_MODULUS = r'%'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COMMA   = r','
t_ENDLINE = r'\;'

###################################### NEWLINE
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

###################################### IGNORES
t_ignore  = ' \t'

t_ignore_COMMENT = r'\#.*'

###################################### ERROR
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

###################################### NUMBERS

def t_lbrace(t):
     r'\.'
     t.type = '.'      # Set token type to the expected literal
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
    if t.value in keywords:
        t.type = t.value
        return t
    elif t.value in booleanOps:
        t.type = t.value
        return t
    elif t.value in hits:
        t.type = t.value
        return t
    else:
        t_error(t)



def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)    
    return t

def t_VAR(t):
    r'@([a-zA-Z_0-9]|_|\?){3,10}'
    t.value = str(t.value)    
    return t

'''
def t_WORD(t):
    r'[a-zA-Z_]+'
    t.value = str(t.value)    
    return t
'''
'''
def t_RESERVED(t):
    #r'@[a-zA-Z_0-9]*'
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'WORD')    # Check for reserved words
    #print('EL TIPOI ES : ' + t.type);
    return t

def t_n(t):
    r'@'
    print('siiii')


'''


 
 # Build the lexer
lexer = lex.lex()


data = ''',{ SET println! If @Aqqaae @var26_? type() .Neg Abanico() ; //% ** 10 -20ab *2\n True False Fin-EnCaso'''
#data = '''3 + 5 * 10 - 20 '''
#data = 'a = 3'
#data = '1 + 5\nabce\n77\nif yo'

 # Give the lexer some input
lexer.input(data)
 
 # Tokenize
for tok in lexer:
     #print(tok)
     print("Class:"+tok.type+" Value:"+str(tok.value)+" Line:"+str(tok.lineno)+" Pos:"+str(tok.lexpos))




