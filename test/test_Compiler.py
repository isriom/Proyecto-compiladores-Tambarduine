import logging
from datetime import datetime
import src
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


def test_if():
	code = "	if True: \n\txyz=5"

	example = "if True {SET @xyz,5;};"

	assert compiler.Parse(example) != None


def test_if_else():
	example = "	if True {SET @xyz,5;} else{SET @xyz,5;};"
	assert compiler.Parse(example) is not None


def test_if_false():
	code = "	if True: \n\txyz=5"

	example = "if True {SET @xyz,5;}"

	assert compiler.Parse(example) == None


def test_if_else_false():
	example = "	if True {SET @xyz,5} else{SET @xyz,5;};"
	assert compiler.Parse(example) == None


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
