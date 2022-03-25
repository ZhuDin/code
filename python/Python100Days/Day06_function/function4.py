from pydoc import locate
from threading import local
import time
import shutil
import os

seconds = time.time()
print(seconds)
localtime = time.localtime(seconds)
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
asctime = time.asctime(localtime)
print(asctime)
strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
print(strtime)
mydate = time.strptime('2022-03-25', '%Y-%m-%d')
print(mydate)

shutil.copy('./test/a.txt', './test/a-copy.txt')
os.system('dir')
os.chdir('./test')
os.system('dir')
