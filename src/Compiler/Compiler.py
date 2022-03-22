from libs.ply.lex import LexToken
from libs.ply.yacc import YaccSymbol
from src.Lexxer.Lex import *
from src.ProjectParser.Parser import *


class Scope:
	def __init__(self, t):
		self.variables = {}
		self.lineno = t.lineno
		self.lexpos = t.lexpos
		self.previous = None
		self.toCheck = []
		self.toCheckFor = []
		self.toCheckConditions = []
		self.code = ''

		pass

	def SetLineno(self, t):
		self.lineno = t.lineno
		self.lexpos = t.lexpos

	def GetType(self, t):
		if not (t in self.variables):
			return None
		else:
			return self.variables[t].TYPEOF

	def insert(self, t):
		if type(t[1]) == str:
			self.variables[t[0]] = t[1]
		else:
			tmpvalue = self.GetType(t[1].value)
			if tmpvalue == None:
				self.insertCheck(('ADJUST', t[0], t[1]))
			self.variables[t[0]] = tmpvalue

	def insertCheck(self, checkTuple):
		if checkTuple[0] == 'CON' or checkTuple[0] == 'NUMBER':
			self.toCheckcon.append(checkTuple)
		elif checkTuple[0] == 'FOR':
			self.toCheckfor.append(checkTuple)
		else:
			self.toCheck.append(checkTuple)

	def AddScope(self, scope):
		self.previous = scope
		pass


class Compiler:

	def __init__(self):
		self.Scopes = {'actualScope': None, 'globalScope': None, 'all': []}
		self.lexer = GetLexer()
		self.parser = GetParser()
		self.parser.Comp = self
		self.tablevel = 0
		self.Code = '\n'
		self.status: tuple = ("Init complete",)
		self.errors: str = ''

	def Parse(self, text):
		self.status = ("inited",)
		self.errors = ''
		parse = self.parser.parse(text, debug=True)
		self.code = self.readTree(parse)
		print(self.code)
		if self.errors == '':
			self.errors += 'No se han encontrado errores en el codigo'
		self.status = ("Compilacion finalizada", 'Errores' + self.errors)

		return parse

	def GetCode(self):
		return GetCode()

	def Gettype(self, t):
		if self.Scopes['actualScope'] is not None:
			return self.Scopes['actualScope'].GetType(t)
		else:
			return None

	def Insert(self, T):
		self.Scopes['actualScope'].insert(T)

	def insertCheck(self, checkTuple):
		self.Scopes['actualScope'].insertCheck(checkTuple)

	def AddGlobal(self, Scope):
		if self.Scopes['globalScope'] != None:
			raise SyntaxError
		else:
			self.Scopes['globalScope'] = Scope
		pass

	def CreateScope(self, T):
		new = Scope(T)
		if self.Scopes['actualScope'] != None:
			self.Scopes['actualScope'].AddScope(new)
		self.Scopes['all'].append(new)
		self.Scopes['actualScope'] = new
		return new

	def CloseScope(self):
		if self.Scopes['actualScope'].previous != None:
			self.Scopes['actualScope'] = self.Scopes['actualScope'].previous

	def readTree(self, ast, tablevel=0):
		if ast is None:
			return
		if type(ast) == YaccSymbol:
			ast = ast.value
		if type(ast) == LexToken:
			ast = (ast.type, ast.value, ast)
		length = len(ast)

		Code = ''
		if ast[0] == 'ENDLINE':
			return ''
		if ast[0] == ':':
			return ''
		elif ast[0] == 'instruction':
			for instruction in range(1, length):
				Code += self.readTree(ast[instruction], tablevel)

		elif ast[0] == 'ifelsestatement':
			Code += ("\t" * tablevel) + self.readTree(ast[1], tablevel) + '\n'
			Code += ("\t" * tablevel) + self.readTree(ast[2], tablevel)

		elif ast[0] == 'elsestatement':
			Code += ("\t" * tablevel) + "Else" + ":\n"
			Code += ("\t" * tablevel) + self.readTree(ast[2], tablevel + 1)

		elif ast[0] == 'ifstatement':
			Code += ("\t" * tablevel) + "if " + self.readTree(ast[2]) + ":\n"
			Code += ("\t" * tablevel) + self.readTree(ast[3], tablevel + 1)

		elif ast[0] == 'forstatement':  # need a refactor
			if ast[2].defined == 'FOR' or ast[2].defined == None:
				Code += ("\t" * tablevel) + "for " + self.readTree(ast[2]) + 'in range( 1,' + self.readTree(ast[4])
			else:
				Code += ("\t" * tablevel) + "for " + self.readTree(ast[2]) + ' in range(' + self.readTree(
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
				Code += ("\t" * tablevel) + self.readTree(ast[4], tablevel + 1) + '\n'
			else:
				Code += 'Principal()' + ':\n'
				Code += ("\t" * tablevel) + self.readTree(ast[5], tablevel + 1) + '\n'

		elif ast[0] == 'excecstatement':
			Code += ("\t" * tablevel) + self.readTree(ast[2]) + self.readTree(ast[3]) + "\n"

		elif ast[0] == 'printstatement':
			Code += ("\t" * tablevel) + 'print' + self.readTree(ast[2]) + "\n"

		elif ast[0] == 'metronomostatement':
			Code += ("\t" * tablevel) + 'Pandereta.Metronomo(' + self.readTree(ast[3]) + ',' + self.readTree(
				ast[5]) + ")\n"

		elif ast[0] == 'declarationstatement':
			Code += ("\t" * tablevel) + self.readTree(ast[2]) + '=' + self.readTree(ast[4]) + "\n"

		elif ast[0] == 'negationstatement':
			Code += ("\t" * tablevel) + self.readTree(ast[2]) + '=not ' + self.readTree(ast[2]) + "\n"

		elif ast[0] == 'tfstatement':
			Code += ("\t" * tablevel) + self.readTree(ast[2]) + '=True ' + "\n"

		elif ast[0] == 'ffstatement':
			Code += ("\t" * tablevel) + self.readTree(ast[2]) + '=False ' + "\n"

		elif ast[0] == 'abanicostatement':
			Code += ("\t" * tablevel) + 'Pandereta.abanico(' + self.readTree(ast[3]) + ")\n"

		elif ast[0] == 'verticalstatement':
			Code += ("\t" * tablevel) + 'Pandereta.vertical(' + self.readTree(ast[3]) + ")\n"

		elif ast[0] == 'percutorstatement':
			Code += ("\t" * tablevel) + 'Pandereta.percutor(' + self.readTree(ast[3]) + ")\n"

		elif ast[0] == 'golpestatement':
			Code += ("\t" * tablevel) + "Pandereta.golpe()\n"

		elif ast[0] == 'vribatoestatement':
			Code += ("\t" * tablevel) + 'Pandereta.percutor(' + self.readTree(ast[3]) + ")\n"

		elif ast[0] == 'typeestatement':
			Code += ("\t" * tablevel) + 'type(' + self.readTree(ast[3]) + ")\n"

		elif ast[0] == 'expressionestatement':
			Code += ("\t" * tablevel) + self.readTree(ast[1])

		elif ast[0] == 'Scope':
			Code += self.readTree(ast[3], tablevel)

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

		elif ast[0] == 'Parameters':
			Code += self.readTree(ast[1]) + self.readTree(ast[2])

		elif ast[0] == 'ParameterIncomplete':
			if length == 3:
				Code += self.readTree(ast[1]) + self.readTree(ast[2])
			else:
				Code += self.readTree(ast[1]) + ',' + self.readTree(ast[3])

		elif ast[0] == 'text':
			Code += self.readTree(ast[1]) + self.readTree(ast[2])

		elif ast[0] == 'textincomplete':
			Code += self.readTree(ast[1]) + ' ' + self.readTree(ast[2])

		elif ast[0] == 'var':
			Code += self.readTree(ast[1])

		elif ast[0] == 'numberParam':
			if length == 3:
				Code += self.readTree(ast[1]) + self.readTree(ast[2])
			elif length == 4:
				Code += self.readTree(ast[1]) + self.readTree(ast[2]) + self.readTree(ast[3])
			else:
				Code += self.readTree(ast[1])

		elif ast[0] == 'boolParam':
			Code += self.readTree(ast[1])

		elif ast[0] == 'condition':
			Code += self.readTree(ast[1])

		elif ast[0] == 'Pre_Scope':
			Code += ''

		elif ast[0] == 'expression':
			Code += self.readTree(ast[1]) + self.readTree(ast[2]) + self.readTree(ast[3])

		elif ast[0] == 'bool':
			if length == 4:
				Code += self.readTree(ast[1]) + self.readTree(ast[2]) + self.readTree(ast[3])
			else:
				Code += self.readTree(ast[1])

		elif ast[0] == 'VAR':
			Code += ast[1][1:] + ' '

		elif ast[0] == 'NUMBER':
			Code += str(ast[1])

		else:
			return ast[1]
		return Code

	def ENCASO(self, ast, tablevel, parametro):
		if type(ast) != tuple:
			ast = ast.value
		length = len(ast)
		Code = ''
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

		'''Def @MiRutina2 ()
		{ Set @xy1, 4; }
		Def @MiRutina (@dato1) 
		 { println! ("Desde la rutina  ", @dato1 );
		 Exec @MiRutina2();
		 Set @Var1, 1;
		for @Var1 to 10 Step 2
		{ println! ("Valor: ", @Var1 ); }
		 }
		Def Principal () 
		{
		Set @Variable1, 5; # Variables globales
		Set @xy1, 20;
		Set @yx3, 15;
		Set @variable, False;
		Set @variable.NEG;
		Exec @MiRutina(2);
		Exec @MiRutina(@Variable1);
		}''')

	File = open("Rutina.py", "w")
	comp.code += '\nPrincipal()'
	File.write(comp.code)
	File.close()
	print('ast')
	print(ast)
