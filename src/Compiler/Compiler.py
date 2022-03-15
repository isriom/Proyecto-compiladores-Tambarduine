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
		if ast is None:
			return
		if type(ast) != tuple:
			print(ast.__dict__)
			ast = ast.value
		length = len(ast)

		Code = ''
		if ast[0] == ';':
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
			Code += ("\t" * tablevel) + "FOR" + self.readTree(ast[2]) + 'TO' + self.readTree(ast[4])
			if length > 6:
				Code += 'STEP' + self.readTree(ast[6])
				Code += ("\t" * tablevel) + self.readTree(ast[7], tablevel + 1)
			else:
				Code += ("\t" * tablevel) + self.readTree(ast[5], tablevel + 1)

		elif ast[0] == 'incasestatement':
			if length == 5:
				Code += ("\t" * tablevel) + self.readTree(ast[2])
				Code += ("\t" * tablevel) + self.readTree(ast[3])
			else:
				Code += self.ENCASO(ast[3], tablevel, self.readTree(ast[2]))

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
		'EnCaso @var Cuando >5 EnTons{SET @var2,10;} Cuando >7 EnTons{SET @var3,10;}SiNo{SET @var3,20;} Fin-EnCaso;')
	print('ast')
	print(ast)
