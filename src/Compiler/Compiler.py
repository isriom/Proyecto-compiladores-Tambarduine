from libs.ply.yacc import YaccSymbol
from src.Lexxer.Lex import *
from src.ProjectParser.Parser import *

# from src.Reglas.REGLAS import *

Input = '''
SET @xyz, 15;
if @xyz<10 {
println!(@xyz)
}

'''


class Scope:
	def __init__(self, t):
		self.variables = {}
		self.lineno = t.lineno
		self.lexpos = t.lexpos
		self.previous = None
		self.toCheck = []
		self.toCheckcon = []

		pass

	def SetLineno(self, t):
		self.lineno = t.lineno
		self.lexpos = t.lexpos

	def GetType(self, t):
		if not (t.value in self.variables):
			self.toCheck += [t]
			return 'NAME'
		else:
			return self.variables[t]['TYPE']

	def insert(self, t):

		if type(t[4]) is str:
			self.variables[t[2]] = {'TYPE': 'BOOLEAN'}
		else:
			self.variables[t[2]] = {'TYPE': type(t[4])}
		print(self.__dict__)
		pass

	def AddScope(self, scope):
		self.previous = scope
		pass

	def insertCheck(self, t, c, t2):
		self.toCheck += [(t, c, t2)]


class Compiler:

	def __init__(self):
		self.Scopes = {'actualScope': None, 'globalScope': None}
		self.lexer = GetLexer()
		self.parser = GetParser()
		self.parser.Comp = self
		self.tablevel = 0
		self.Code = ''

	def Parse(self, text):
		parse = self.parser.parse(text, debug=True)
		self.readTree(parse)
		return parse

	def GetCode(self):
		return GetCode()

	def Gettype(self, t):
		if self.Scopes['actualScope'] is not None:
			return self.Scopes['actualScope'].GetType(t)
		else:
			return None

	def Insert(self, T):
		print(T.__dict__)
		self.Scopes['actualScope'].insert(T)

	def AddGlobal(self, scope):
		self.Scopes['globalScope'] = scope
		pass

	def CreateScope(self, T):
		if Compiler().Scopes['actualScope'] is None:
			print(comp)
			Compiler().Scopes['actualScope'] = Scope(T)
		else:
			Compiler().Scopes['actualScope'].addScope(self)

	def insertCode(self, code):
		code += '\n'

	def readTree(self, ast, tablevel=0):
		length = 0
		if ast is None:
			return
		if type(ast) == YaccSymbol:
			print(ast.__dict__)
			ast = ast.value
		if type(ast) == LexToken:
			print(ast.__dict__)
			ast = (ast.type, ast.value, ast)
		length = len(ast)

		Code = ''
		if ast[0] == 'ENDLINE':
			return ''
		if ast[0] == ':':
			return ''
		elif ast[0] == 'instruction':
			for instruction in range(1, length):
				Code += ("\t" * tablevel) + self.readTree(ast[instruction], tablevel)

		elif ast[0] == 'ifelsestatement':
			Code += ("\t" * tablevel) + self.readTree(ast[1], tablevel) + '\n' + ("\t" * tablevel) + self.readTree(
				ast[2], tablevel)

		elif ast[0] == 'elsestatement':
			Code += ("\t" * tablevel) + "Else" + ":\n"
			Code += ("\t" * tablevel) + self.readTree(ast[2], tablevel + 1)

		elif ast[0] == 'ifstatement':
			Code += ("\t" * tablevel) + "if" + self.readTree(ast[2]) + ":\n"
			Code += ("\t" * tablevel) + self.readTree(ast[3], tablevel + 1)

		elif ast[0] == 'forstatement':
			print(ast[2].__dict__)
			if ast[2].defined == None:
				Code += ("\t" * tablevel) + "FOR " + self.readTree(ast[2]) + 'in range( 1,' + self.readTree(ast[4])
			else:
				Code += ("\t" * tablevel) + "FOR " + self.readTree(ast[2])[:-2] + ' in range(' + self.readTree(
					ast[2]) + ',' + self.readTree(ast[4])
			if length > 6:
				Code += ',' + self.readTree(ast[6])
				Code += '):\n' + ("\t" * tablevel) + self.readTree(ast[7], tablevel + 1)
			else:
				Code += '):\n' + ("\t" * tablevel) + self.readTree(ast[5], tablevel + 1)

		elif ast[0] == 'incasestatement':
			if length == 5:
				Code += ("\t" * tablevel) + self.readTree(ast[2])
				Code += ("\t" * tablevel) + self.readTree(ast[3])
			else:
				Code += self.ENCASO(ast[3], tablevel, self.readTree(ast[2]))

		elif ast[0] == 'defstatement':
			Code += ("\t" * tablevel) + 'def '
			if length == 5:
				Code += self.readTree(ast[2]) + self.readTree(ast[3]) + ':\n'
				Code += ("\t" * tablevel) + self.readTree(ast[4]) + '\n'
			else:
				Code += 'Principal()' + ':\n'
				Code += ("\t" * tablevel) + self.readTree(ast[5]) + '\n'

		elif ast[0] == 'excecstatement':
			Code += ("\t" * tablevel) + self.readTree(ast[2]) + self.readTree(ast[3]) + ":\n"

		elif ast[0] == 'printstatement':
			Code += ("\t" * tablevel) + 'print(' + self.readTree(ast[2]) + ")\n"

		elif ast[0] == 'metronomostatement':
			Code += ("\t" * tablevel) + 'Pandereta.Metronomo(' + self.readTree(ast[3]) + ',' + self.readTree(
				ast[5]) + ")\n"


		elif ast[0] == 'declarationstatement':
			Code += ("\t" * tablevel) + self.readTree(ast[2]) + '=' + self.readTree(ast[4])
			"\n"


		elif ast[0] == 'negationstatement':
			Code += ("\t" * tablevel) + self.readTree(ast[2]) + '=not ' + self.readTree(ast[2]) + "\n"


		elif ast[0] == 'whenestatement':
			if length <= 3:
				Code += ("\t" * tablevel) + self.readTree(ast[1])
				Code += ("\t" * tablevel) + self.readTree(ast[2])
			else:
				Code += ("\t" * tablevel) + "if" + self.readTree(ast[2]) + self.readTree(ast[3]) + self.readTree(
					ast[4]) + ":\n"
				Code += ("\t" * tablevel) + self.readTree(ast[6], tablevel + 1)

		elif ast[0] == 'whenelseestatement':
			Code += ("\t" * tablevel) + "Else" + ":\n"
			Code += ("\t" * tablevel) + self.readTree(ast[2], tablevel + 1)

		elif ast[0] == 'Scope':
			Code += self.readTree(ast[3])

		else:
			return " " + ast[0] + " "
		print(Code)
		return Code

	def ENCASO(self, ast, tablevel, parametro):
		if type(ast) != tuple:
			print(ast.__dict__)
			ast = ast.value
		length = len(ast)
		Code = ''
		print(ast)
		if length <= 3:
			Code += ("\t" * tablevel) + self.ENCASO(ast[1], tablevel, parametro)
			Code += ("\t" * tablevel) + self.ENCASO(ast[2], tablevel, parametro)
		else:
			Code += ("\t" * tablevel) + "if" + parametro + self.readTree(ast[2]) + self.readTree(ast[3]) + ":\n"
			Code += ("\t" * tablevel) + self.readTree(ast[5], tablevel + 1) + "\n"
		return Code
		pass


if __name__ == '__main__':
	comp = Compiler()
	ast = comp.Parse(
		'for @xyz to 15 Step 15{SET @mdd,15;};')
	print('ast')
	print(ast)
