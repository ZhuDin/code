import os, json

os.chdir(os.path.dirname(__file__))

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
