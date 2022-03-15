from src.Compiler.Compiler import *
from src.Compiler.Compiler import Scope, Compiler


def p_REGLA_89(p):
	'''
	Pre_Scope :
	'''
	scope = p.parser.Comp.CreateScope(T=p.stack[-1])
	p[0] = ()


def p_REGLA_70(p):
	'''
	var : VAR
	'''
	Type = p.parser.Comp.Gettype(p[1])
	if Type == 'BOOLEAN':
		p.slice[0].value = p.slice[1].value
	elif Type == 'NUM':
		p.slice[0].value = p.slice[1].value
	else:
		p.slice[0].value = p.slice[1].value

	p[0] = (p[1])

