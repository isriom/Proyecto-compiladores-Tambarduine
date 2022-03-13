from src.Compiler.Compiler import *
from src.Compiler.Compiler import Scope, Compiler


def p_REGLA_89(p):
	'''
	Pre_Scope :
	'''
	scope = p.parser.Comp.CreateScope(T=p.stack[-1])
	print(scope)
	print(p.stack[-1].__dict__)
	print(p.__dict__)
	p[0] = ()


def p_REGLA_70(p):
	'''
	var : VAR
	'''
	Type = p.parser.Comp.gettype(p[1])
	if Type == 'BOOLEAN':
		p.slice[0].type = 'varbool'
		p.slice[0].value = p.slice[1].value
	elif Type == 'NUM':
		p.slice[0].type = 'varnum'
		p.slice[0].value = p.slice[1].value

	else:
		p.slice[0].type = 'var'
		p.slice[0].value = p.slice[1].value
	p[0] = (p[1])


def p_REGLA_71(p):
	'''
	varbool : NAME
	'''
	Type = p.parser.Comp.gettype(p[1])
	p.stack[-1] = Type
	p[0] = (p[1])
