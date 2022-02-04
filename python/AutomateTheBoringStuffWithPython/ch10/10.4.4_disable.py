import logging
logging.basicConfig(level=logging.INFO,
    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.critical('Critical error! Critical error! first!')
logging.disable(logging.CRITICAL)
logging.critical('Critical error! Critical error! second!')
logging.error('Error! Error!')
