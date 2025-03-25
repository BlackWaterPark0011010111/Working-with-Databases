# inheritance
# interface.
# composition.

class Car:
    year = "2015"
    color = "black"
    material = "iron"
    name = "Toyota"

    def get_name(self):
        print(self.color + self.year)

class Furniture:
    chair_type = "leather"
    chair_design = "topnotch"

# inheriting without changing anything  
class Corrola(Car):
    pass

# car_a = Car()
# car_b = Car()

# corrolla_a = Corrola()
# corrolla_b = Corrola()

# print(car_a.color)
# print(car_b.color)
# print("\n")
# print(corrolla_a.color)
# print(corrolla_b.color)
# print(corrolla_a.get_name())


class CorrollaBig(Car, Furniture):
    color = "Red"
    # def get_name(self):
    #     print("Not what you are looking for ")
    def get_name(self):
        # you must try to use the old method.
        # 1. calling the parent class directly
        # 2. calling the super class
        # Car.get_name(self)
        # super().get_name()
        print("Not what you are looking for ")
    
    def get_color(self):
        print("wow you have a nice color")

car_a = Car()
car_b = Car()

corrolla_a = CorrollaBig()
corrolla_b = CorrollaBig()

print(car_a.color)
print(car_b.color)
print("\n")
print(corrolla_a.color)
print(corrolla_b.color)
print(corrolla_a.get_color())
print(corrolla_a.chair_type)