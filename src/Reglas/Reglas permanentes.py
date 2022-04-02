from src.Compiler.Compiler import *
from src.Compiler.Compiler import Scope, Compiler
from src.Reglas.REGLAS import *


def p_REGLA_24(p):
	'''
	forstatement : FOR VAR TO numberParam STEP numberParam Scope
	'''
	p.parser.Comp.insertCheck(('FOR', p.slice[2]))
	p.slice[7].scope.insert((p[2], 'NUMBER'))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3], p.slice[4], p.slice[5], p.slice[6], p.slice[7])


def p_REGLA_25(p):
	'''
	forstatement : FOR var TO numberParam STEP numberParam Scope
	'''
	p.parser.Comp.insertCheck(('FOR', p.slice[2], 'foo'))
	p.slice[7].scope.insert((p[2], 'NUMBER'))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3], p.slice[4], p.slice[5], p.slice[6], p.slice[7])


def p_REGLA_26(p):
	'''
	forstatement : FOR VAR TO numberParam Scope
	'''
	p.parser.Comp.insertCheck(('FOR', p.slice[2]))
	p.slice[5].scope.insert((p[2], 'NUMBER'))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3], p.slice[4], p.slice[5])


def p_REGLA_27(p):
	'''
	forstatement : FOR var TO numberParam Scope
	'''
	p.parser.Comp.insertCheck(('FOR', p.slice[2], 'foo'))
	p.slice[5].scope.insert((p[2], 'NUMBER'))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3], p.slice[4], p.slice[5])


def p_REGLA_31(p):
	'''
	defstatement : DEF VAR Parameters Scope
	'''
	for i in range(1, p.slice[3].vars):
		p.parser.Comp.RemoveCheck()
	p.slice[4].scope.insert(('PARAM', p[3]))
	p.parser.Comp.Insert((('def', p.slice[2]), str(p.slice[3].number)))
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3], p.slice[4])


def p_REGLA_32(p):
	'''
	defstatement : DEF PRINCIPAL LPAREN RPAREN Scope
	'''
	p.parser.Comp.AddGlobal(p.slice[5].scope)
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3], p.slice[4], p.slice[5])


def p_REGLA_33(p):
	'''
	excecstatement : EXEC VAR Parameters
	'''
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])
	p.parser.Comp.insertCheck((p[1], p[2], p.slice[3]))


def p_REGLA_37(p):
	'''
	declarationstatement : SET var COMMA numberParam
	'''
	p.parser.Comp.Insert((p[2], 'NUMBER'))
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3], p.slice[4])


def p_REGLA_38(p):
	'''
	declarationstatement : SET var COMMA boolParam
	'''
	p.parser.Comp.Insert((p[2], 'BOOL'))
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3], p.slice[4])


def p_REGLA_39(p):
	'''
	declarationstatement : SET var COMMA NUMBER
	'''
	p.parser.Comp.Insert((p[2], 'NUMBER'))
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3], p.slice[4])


def p_REGLA_40(p):
	'''
	declarationstatement : SET var COMMA var
	'''
	p.parser.Comp.Insert((p[2], p.slice[4]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3], p.slice[4])


def p_REGLA_41(p):
	'''
	negationstatement : SET var DOT NEG
	'''
	p.parser.Comp.insertCheck(('NEG', p[2]))
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3], p.slice[4])


def p_REGLA_42(p):
	'''
	tfstatement : SET var DOT T
	'''
	p.parser.Comp.Insert((p[2], 'bool'))
	p.parser.Comp.insertCheck(('T', p[2]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3], p.slice[4])


def p_REGLA_43(p):
	'''
	ffstatement : SET var DOT F
	'''
	p.parser.Comp.Insert((p[2], 'bool'))
	p.parser.Comp.insertCheck(('F', p[2]))
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3], p.slice[4])


def p_REGLA_58(p):
	'''
	Scope : LSCOPE Pre_Scope instruction RSCOPE
	'''
	p.slice[0].scope = p.slice[2].scope
	p.parser.Comp.CloseScope()

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3], p.slice[4])


def p_REGLA_67(p):
	'''
	Parameters : ParameterIncomplete RPAREN
	'''
	p.slice[0].vars = p.slice[1].vars
	p.slice[0].number = p.slice[1].number
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[1].number)


def p_REGLA_68(p):
	'''
	Parameters : LPAREN RPAREN
	'''

	p.slice[0].vars = 0
	p.slice[0].number = 0
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2])


def p_REGLA_69(p):
	'''
	ParameterIncomplete : ParameterIncomplete COMMA numberParam
	'''
	p.slice[0].vars = p.slice[1].vars
	p.slice[0].number = p.slice[1].number + 1
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_70(p):
	'''
	ParameterIncomplete : ParameterIncomplete COMMA var
	'''
	p.slice[0].vars = p.slice[1].vars + 1
	p.slice[0].number = p.slice[1].number + 1
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])
	pass


def p_REGLA_71(p):
	'''
	ParameterIncomplete : ParameterIncomplete COMMA boolParam
	'''
	p.slice[0].vars = p.slice[1].vars
	p.slice[0].number = p.slice[1].number + 1
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_72(p):
	'''
	ParameterIncomplete : ParameterIncomplete COMMA text
	'''
	p.slice[0].vars = p.slice[1].vars
	p.slice[0].number = p.slice[1].number + 1
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_73(p):
	'''
	ParameterIncomplete : ParameterIncomplete COMMA typeestatement
	'''

	p.slice[0].vars = p.slice[1].vars
	p.slice[0].number = p.slice[1].number + 1
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_74(p):
	'''
	ParameterIncomplete : LPAREN numberParam
	'''
	p.slice[0].vars = 0
	p.slice[0].number = 1
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2])


def p_REGLA_75(p):
	'''
	ParameterIncomplete : LPAREN var
	'''
	p.slice[0].vars = 1
	p.slice[0].number = 1
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2])


def p_REGLA_76(p):
	'''
	ParameterIncomplete : LPAREN boolParam
	'''
	p.slice[0].vars = 0
	p.slice[0].number = 1
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2])


def p_REGLA_77(p):
	'''
	ParameterIncomplete : LPAREN text
	'''
	p.slice[0].vars = 0
	p.slice[0].number = 1
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2])


def p_REGLA_78(p):
	'''
	ParameterIncomplete : LPAREN typeestatement
	'''
	p.slice[0].vars = 0
	p.slice[0].number = 1
	p[0] = (p.slice[0].type, p.slice[1], p.slice[2])


def p_REGLA_83(p):
	'''
	var : VAR
	'''
	p.slice[0].defined = p.parser.Comp.Gettype(p[1])
	p.slice[0].globalvar = False

	if p.slice[0].defined is None:
		tupletmp = ('TYPEOF', p[1], p.slice[0])
		p.parser.Comp.insertCheck(('TYPEOF', p[1], p.slice[0]))

	# p.slice[0].value = p.slice[1].value
	p[0] = (p.slice[0].type, p.slice[1], p.slice[0])


def p_REGLA_89(p):
	'''
	bool : numberParam condition numberParam
	'''
	p.parser.Comp.insertCheck(('CON', p.slice[1], p.slice[3], p.slice[2]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_90(p):
	'''
	bool : boolParam condition boolParam
	'''
	p.parser.Comp.insertCheck(('CON', p.slice[1], p.slice[3], p.slice[2]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_98(p):
	'''
	Pre_Scope :
	'''
	Scope = p.parser.Comp.CreateScope(T=p.stack[-1])
	p.slice[0].scope = Scope

	p[0] = (p.slice[0].type)


def p_REGLA_100(p):
	'''
	expression : numberParam PLUS numberParam
	'''
	p.parser.Comp.insertCheck(('NUM', p.slice[1], p.slice[3]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_101(p):
	'''
	expression : numberParam MINUS numberParam
	'''
	p.parser.Comp.insertCheck(('NUM', p.slice[1], p.slice[3]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_102(p):
	'''
	expression : numberParam TIMES numberParam
	'''
	p.parser.Comp.insertCheck(('NUM', p.slice[1], p.slice[3]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_103(p):
	'''
	expression : numberParam DIVIDE numberParam
	'''
	p.parser.Comp.insertCheck(('NUM', p.slice[1], p.slice[3]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_104(p):
	'''
	expression : numberParam INTDIVIDE numberParam
	'''
	p.parser.Comp.insertCheck(('NUM', p.slice[1], p.slice[3]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_105(p):
	'''
	expression : numberParam MODULUS numberParam
	'''
	p.parser.Comp.insertCheck(('NUM', p.slice[1], p.slice[3]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_106(p):
	'''
	expression : numberParam POWER numberParam
	'''
	p.parser.Comp.insertCheck(('NUM', p.slice[1], p.slice[3]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_115(p):
	'''
	expression : expression PLUS numberParam
	'''
	p.parser.Comp.insertCheck(('NUM', p.slice[3]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_116(p):
	'''
	expression : expression MINUS numberParam
	'''
	p.parser.Comp.insertCheck(('NUM', p.slice[3]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_117(p):
	'''
	expression : expression TIMES numberParam
	'''
	p.parser.Comp.insertCheck(('NUM', p.slice[3]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_118(p):
	'''
	expression : expression DIVIDE numberParam
	'''
	p.parser.Comp.insertCheck(('NUM', p.slice[3]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_119(p):
	'''
	expression : expression INTDIVIDE numberParam
	'''
	p.parser.Comp.insertCheck(('NUM', p.slice[3]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_120(p):
	'''
	expression : expression MODULUS numberParam
	'''
	p.parser.Comp.insertCheck(('NUM', p.slice[3]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_121(p):
	'''
	expression : expression POWER numberParam
	'''
	p.parser.Comp.insertCheck(('NUM', p.slice[3]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])


def p_REGLA_122(p):
	'''
	numberParam : MINUS numberParam
	'''
	p.parser.Comp.insertCheck(('NUM', p.slice[2]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2])


def p_REGLA_123(p):
	'''
	numberParam : numberParam DOT numberParam
	'''
	p.parser.Comp.insertCheck(('NUM', p.slice[1], p.slice[3]))

	p[0] = (p.slice[0].type, p.slice[1], p.slice[2], p.slice[3])
