from src.Lexxer.Lex import *
from src.ProjectParser.Parser import *

# from src.Reglas.REGLAS import *

Input = '''
SET @xyz, 15;
if @xyz<10 {
println!(@xyz)
}

'''


class Compiler:
	def __init__(self):
		self.lexer = GetLexer()
		self.parser = GetParser()

	def Parse(self, text):
		parse = self.parser.parse(text)
		return parse

	def GetCode(self):
		return GetCode()



# lexer = GetLexer()
# parser = GetParser()
# ast = parser.parse('if True {SET @xyz,5;} else {SET @xyz,5;};', debug=True)
# print(ast)
