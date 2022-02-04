class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year 

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

your_new_car = Car('audi', 'a4', 2021)
my_new_car = Car('BMW', 'C260', 2022)
print(my_new_car.get_descriptive_name())
