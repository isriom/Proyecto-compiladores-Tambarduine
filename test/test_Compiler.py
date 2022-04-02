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
	code = "xyz =5\n"

	example = "Def Principal(){SET @xyz,5;}"

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_declaration_bool():
	code = "xyz =False\n"

	example = "Def Principal(){SET @xyz,False;}"

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_declaration_number_false():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){SET @bxy,A;}"

	assert compiler.Parse(example) == None
	assert compiler.errors != 'No se han encontrado errores en el codigo'


def test_declaration_bool_false():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){SET @xyz False;}"

	assert compiler.Parse(example) == None
	assert compiler.errors != 'No se han encontrado errores en el codigo'


def test_type_bool():
	code = "xyz =True\ntype(xyz )\n"

	example = "Def Principal(){SET @xyz,True; type(@xyz);}"

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_type_num():
	code = "xyz =(5+2/2)\ntype(xyz )\n"

	example = "Def Principal(){SET @xyz, (5+2/2); type(@xyz);}"

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_arithmetic():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){Set @x12,1;Set @y32,1;(@x12 +@y32)*10/4;}"

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_Neg():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){Set @x12, True; Set @x12.Neg; Set @x12.Neg;}"

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_T():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){Set @x12.T;}"

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_F():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){Set @x12.F;}"

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_Abanico():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){Abanico(A);Abanico(B);}"

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_Abanico_false():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){Abanico(A);Abanico(C);}"

	assert compiler.Parse(example) == None
	assert compiler.errors != 'No se han encontrado errores en el codigo'


def test_Vertical():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){Vertical(I);Vertical(D);}"

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_Vertical_false():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){Vertical(I);Vertical(C);}"

	assert compiler.Parse(example) == None
	assert compiler.errors != 'No se han encontrado errores en el codigo'


def test_Percutor():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){Percutor(D);Percutor(I);Percutor(DI);Percutor(A);Percutor(B);Percutor(AB);}"

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_Percutor_false():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){Percutor(D);Percutor(I);Percutor(DI);Percutor(A);Percutor(B);Percutor(AC);}"

	assert compiler.Parse(example) == None
	assert compiler.errors != 'No se han encontrado errores en el codigo'


def test_Vibrato():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){Vibrato(1);}"

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_Vibrato_false():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){Vibrato(True);}"

	assert compiler.Parse(example) == None
	assert compiler.errors != 'No se han encontrado errores en el codigo'


def test_Metronomo():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){Metronomo(A,0.5);}"

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_Metronomo_false():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){Metronomo(E,0.5);}"

	assert compiler.Parse(example) == None
	assert compiler.errors != 'No se han encontrado errores en el codigo'


def test_Golpe():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){Golpe();}"

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_Golpe_false():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){Golpe(A);}"

	assert compiler.Parse(example) == None
	assert compiler.errors != 'No se han encontrado errores en el codigo'


def test_print():
	code = "	if True: \n\txyz=5"

	example = 'Def Principal(){SET @curso, 1;println!("este es el proyecto numero",@curso,"de compiladores. Y la variable curso es:",type(@curso));}'

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_for():
	code = "	if True: \n\txyz=5"

	example = 'Def Principal(){for @xyz to 15{SET @mdf,15;}}'

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_for_var():
	code = "	if True: \n\txyz=5"

	example = 'Def Principal(){SET @xyz,15;for @xyz to 15{SET @mdf,15;}}'

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_for_step():
	code = "	if True: \n\txyz=5"

	example = 'Def Principal(){for @xyz to 15 Step 15{SET @mdd,15;}}'

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_for_var_step():
	code = "	if True: \n\txyz=5"

	example = 'Def Principal(){SET @xyz,15;for @xyz to 15 Step 15{SET @mdf,15;}}'

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_if():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){if True {SET @xyz,5;};}"

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


##Falta procesar == en el parser##
def test_if_else():
	example = "	Def Principal(){SET @xym,5;if @xym*2==6 {SET @xyz,5;} else{SET @xyz,5;};}"
	assert compiler.Parse(example) is not None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_if_false():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){if True {SET @xyz,5;}}"

	assert compiler.Parse(example) == None
	assert compiler.errors != 'No se han encontrado errores en el codigo'


def test_if_else_false():
	example = "	Def Principal(){if @xyz {SET @xyz,5} else{SET @xyz,5;};}"
	assert compiler.Parse(example) == None
	assert compiler.errors != 'No se han encontrado errores en el codigo'


def test_Cuando():
	code = "	if True: \n\txyz=5"

	example = "Def Principal(){SET @var,10;EnCaso Cuando @var >5 EnTons{SET @var2,10;}Cuando @var >5 EnTons{SET @var2,10;}SiNo{SET @var2,20;}Fin-EnCaso;}"

	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_Cuando_var():
	example = "Def Principal(){SET @var,10;EnCaso @var Cuando >5 EnTons{SET @var2,10;} Cuando >7 EnTons{SET @var3,10;}SiNo{SET @var3,20;} Fin-EnCaso;}"
	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


##Falta agregar letras sueltas como parametros¿?##
def test_Rutina():
	example = "Def Principal(){SET @var,10;}Def @Rutina(@par1,@par2,@par3){SET @var2,20;}"
	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


def test_Exce():
	example = "Def @Rutina(){SET @var2,20;}Def Principal(){Exec @Rutina();}"
	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'


##Falta detectar si la rutina esta declarada##
def test_Exce_false():
	example = "Def Principal(){Exec @Rutina(1,2,3);}"
	assert compiler.Parse(example) != None
	assert compiler.errors != 'No se han encontrado errores en el codigo'


def test_Principal():
	example = "Def Principal(){SET @var2,20;}"
	assert compiler.Parse(example) != None
	assert compiler.errors == 'No se han encontrado errores en el codigo'
