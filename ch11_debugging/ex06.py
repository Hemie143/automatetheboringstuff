import logging


logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s -  %(message)s')
logging.critical('Critical error! Critical error!')
# 2019-05-22 11:10:48,054 - CRITICAL - Critical error! Critical error!

logging.disable(logging.CRITICAL)
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')
