

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
		self.comp = Compiler.instance
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

	def Parse(self, text):
		parse = self.parser.parse(text, debug=True)
		return parse

	def GetCode(self):
		return GetCode()

	def Gettype(self, t):
		return self.Scopes['actualScope'].GetType(t)

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


if __name__ == '__main__':
	comp = Compiler()
	ast = comp.Parse('if True {SET @xyz,5;};')
	print('ast')
	print(ast)
