import os
os.chdir(os.path.dirname(__file__))

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)