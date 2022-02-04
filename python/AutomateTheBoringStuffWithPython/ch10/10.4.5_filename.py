import logging

logging.basicConfig(
    filename='.\python\\AutomateTheBoringStuffWithPython\\ch10\\myProgramLog.txt', 
    level=logging.DEBUG,
    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug("test logging filename")