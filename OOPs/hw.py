class Vehicle:
    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_weight(self, weight):
        self.weight = weight

    def get_description(self):
        return self.year + " " + self.make + " " + self.model


class Car(Vehicle):
    def set_num_doors(self, num_doors):
        self.num_doors = num_doors

    def get_description(self):
        return self.num_doors + "-door " + Vehicle.get_description(self)


class Truck(Vehicle):
    def set_size(self, size):
        self.size = size

    def get_description(self):
        return self.size + " size " + Vehicle.get_description(self)

car = Car()
car.set_make("Toyota")
car.set_model("Camry")
car.set_year("2020")
car.set_weight(3000)
car.set_num_doors("4")
print(car.get_description())

truck = Truck()
truck.set_make("Ford")
truck.set_model("F-150")
truck.set_year("2021")
truck.set_weight(5000)
truck.set_size("short")
print(truck.get_description())