import os
os.chdir(os.path.dirname(__file__))

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write('I love programming.')
