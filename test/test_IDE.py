import logging
from datetime import datetime
LOG_NAME='LOG_'+datetime.now()+'.log'
logging.basicConfig(filename=LOG_NAME, format='%(levelname)s; %(message)s', level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M %p')
def func(x):
    logging.info('Function func exec')
    return true


def test_template():
    logging.info('Test test_template exec')
    assert func(1) == true
    logging.info('Test test_template finished.')
    
