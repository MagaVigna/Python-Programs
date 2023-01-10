class Car:

    def __init__(self,name,mileage,color) :
        self.name=name
        self.mileage=mileage
        self.color=color
        self.make='US'

    def print_details(self):
        return f'The car name is {self.name} and its color is {self.color}, it gives {self.mileage} mileage'

    def print_make(self):
        return f'This car {self.name} is made in {self.make}'

    
class BMW(Car):
    
    def set_make(self):
        self.make='India'


class AUDI(Car):

    def set_make(self):
        self.make='China'


carobj=Car('Honda','100','Red')
print(carobj.print_details())
print(carobj.print_make())

bmwobj=BMW('BMW','100','Black')
bmwobj.set_make()
print(bmwobj.print_details())
print(bmwobj.print_make())

audiobj=AUDI('Audi','100','White')
audiobj.set_make()
print(audiobj.print_details())
print(audiobj.print_make())
        