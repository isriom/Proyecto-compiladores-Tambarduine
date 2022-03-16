import logging
from datetime import datetime
import src.Compiler
from src.Compiler.Compiler import Compiler

LOG_NAME = '../logs/LOG_' + datetime.strftime(datetime.now(), '%Y %m %d %H %M') + '.log'
logging.basicConfig(filename=LOG_NAME, format='%(levelname)s; %(message)s', level=logging.DEBUG,
                    datefmt='%m/%d/%Y %I:%M %p')


##Decorator for test and functions (not in use)##
def print_test(func):
	logging.info('Test ' + func.__name__ + ' exec')
	func()
	logging.info('Test ' + func.__name__ + ' finished.')


def print_func(func):
	logging.info('Function ' + func.__name__ + ' exec')
	func()
	logging.info('Function ' + func.__name__ + ' exec')


##Compiler template##
compiler = Compiler()


def test_declaration_number():
	code = "	if True: \n\txyz=5"

	example = "SET @xyz,5;"

	assert compiler.Parse(example) != None


def test_declaration_bool():
	code = "	if True: \n\txyz=5"

	example = "SET @xyz,False;"

	assert compiler.Parse(example) != None


def test_declaration_number_false():
	code = "	if True: \n\txyz=5"

	example = "SET @bxy,A;"

	assert compiler.Parse(example) == None


def test_declaration_bool_false():
	code = "	if True: \n\txyz=5"

	example = "SET @xyz False;"

	assert compiler.Parse(example) == None


def test_type_bool():
	code = "	if True: \n\txyz=5"

	example = "SET @xyz,True; type(@xyz);"

	assert compiler.Parse(example) != None


def test_type_num():
	code = "	if True: \n\txyz=5"

	example = "SET @xyz, (5+2/2); type(@xyz);"

	assert compiler.Parse(example) != None


def test_arithmetic():
	code = "	if True: \n\txyz=5"

	example = "(@x12 +@y32)*10/4;"

	assert compiler.Parse(example) != None


def test_Neg():
	code = "	if True: \n\txyz=5"

	example = "SET @x12, True; SET @x12.Neg; SET @x12.Neg;"

	assert compiler.Parse(example) != None


def test_T():
	code = "	if True: \n\txyz=5"

	example = "SET @x12.T;"

	assert compiler.Parse(example) != None


def test_F():
	code = "	if True: \n\txyz=5"

	example = "SET @x12.F;"

	assert compiler.Parse(example) != None


def test_Abanico():
	code = "	if True: \n\txyz=5"

	example = "Abanico(A);Abanico(B);"

	assert compiler.Parse(example) != None


def test_Abanico_false():
	code = "	if True: \n\txyz=5"

	example = "Abanico(A);Abanico(C);"

	assert compiler.Parse(example) == None


def test_Vertical():
	code = "	if True: \n\txyz=5"

	example = "Vertical(I);Vertical(D);"

	assert compiler.Parse(example) != None


def test_Vertical_false():
	code = "	if True: \n\txyz=5"

	example = "Vertical(I);Vertical(C);"

	assert compiler.Parse(example) == None


def test_Percutor():
	code = "	if True: \n\txyz=5"

	example = "Percutor(D);Percutor(I);Percutor(DI);Percutor(A);Percutor(B);Percutor(AB);"

	assert compiler.Parse(example) != None


def test_Percutor_false():
	code = "	if True: \n\txyz=5"

	example = "Percutor(D);Percutor(I);Percutor(DI);Percutor(A);Percutor(B);Percutor(AC);"

	assert compiler.Parse(example) == None


def test_Vibrato():
	code = "	if True: \n\txyz=5"

	example = "Vibrato(1);"

	assert compiler.Parse(example) != None


def test_Vibrato_false():
	code = "	if True: \n\txyz=5"

	example = "Vibrato(True);"

	assert compiler.Parse(example) == None


def test_Metronomo():
	code = "	if True: \n\txyz=5"

	example = "Metronomo(A,0.5);"

	assert compiler.Parse(example) != None


def test_Metronomo_false():
	code = "	if True: \n\txyz=5"

	example = "Metronomo(E,0.5);"

	assert compiler.Parse(example) == None


##Falta agregar TEXT al keyboard##
def test_print():
	code = "	if True: \n\txyz=5"

	example = 'SET @curso, 1;println!("este es el proyecto numero",@curso,"de compiladores");'

	assert compiler.Parse(example) != None


def test_for():
	code = "	if True: \n\txyz=5"

	example = 'for @xyz to 15{SET @mdf,15;};'

	assert compiler.Parse(example) != None


def test_for_var():
	code = "	if True: \n\txyz=5"

	example = 'SET @xyz,15;for @xyz to 15{SET @mdf,15;};'

	assert compiler.Parse(example) != None


def test_for_step():
	code = "	if True: \n\txyz=5"

	example = 'for @xyz to 15 Step 15{SET @mdd,15;};'

	assert compiler.Parse(example) != None


def test_for_var_step():
	code = "	if True: \n\txyz=5"

	example = 'SET @xyz,15;for @xyz to 15 Step 15{SET @mdf,15;};'

	assert compiler.Parse(example) != None


def test_if():
	code = "	if True: \n\txyz=5"

	example = "if True {SET @xyz,5;};"

	assert compiler.Parse(example) != None


##Falta procesar == en el parser##
def test_if_else():
	example = "	if @xym*2==6 {SET @xyz,5;} else{SET @xyz,5;};"
	assert compiler.Parse(example) is not None


def test_if_false():
	code = "	if True: \n\txyz=5"

	example = "if True {SET @xyz,5;}"

	assert compiler.Parse(example) == None


def test_if_else_false():
	example = "	if @xyz {SET @xyz,5} else{SET @xyz,5;};"
	assert compiler.Parse(example) == None


def test_Cuando():
	code = "	if True: \n\txyz=5"

	example = "EnCaso Cuando @var >5 EnTons{SET @var2,10;}Cuando @var >5 EnTons{SET @var2,10;}SiNo{SET @var2,20;}Fin-EnCaso;"

	assert compiler.Parse(example) != None


def test_Cuando_var():
	example = "EnCaso @var Cuando >5 EnTons{SET @var2,10;} Cuando >7 EnTons{SET @var3,10;}SiNo{SET @var3,20;} Fin-EnCaso;"
	assert compiler.Parse(example) != None


##Falta agregar letras sueltas como parametros¿?##
def test_Rutina():
	example = "Def @Rutina(h,m,a){SET @var2,20;};"
	assert compiler.Parse(example) != None


def test_Exce():
	example = "Def @Rutina(){SET @var2,20;};Exec @Rutina(1,2,3);"
	assert compiler.Parse(example) != None


##Falta detectar si la rutina esta declarada##
def test_Exce_false():
	example = "Exec @Rutina(1,2,3);"
	assert compiler.Parse(example) == None


def test_Principal():
	example = "Def Principal(){SET @var2,20;};"
	assert compiler.Parse(example) != None
