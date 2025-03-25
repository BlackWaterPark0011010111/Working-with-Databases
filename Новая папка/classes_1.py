class Car:
    color = "red" # data
    name = "Toyota"

    def full_name(self, year, other_name=""):
        self.year = year # registered year attribute to somethig
        print(self.color + self.name + other_name)
        
    

# class attributes color, name, full_name
# instance attribute year

car_a = Car()
car_b = Car()
print(car_a.color)
print(car_b.color)
print("\n")
print(car_a.name)
print(car_b.name)
# __dict__ allows you to see all the  registered instance attributes
print(car_a.__dict__)
car_a.full_name("2010")
print(car_a.__dict__)
print(car_b.__dict__)