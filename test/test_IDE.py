import logging
from datetime import datetime

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


##Test template##
def inc(x):
	return x + 1


def test_inc():
	assert inc(3) == 5

##IDE Test##
