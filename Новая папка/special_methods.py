# 1. create an object with default instance attribute (Constructor) __init__

# 2. printing an object __str__ and __repr__

# 3. making an object behave like a function __call__

class Person:
    country = "Germany"
    language = "English"

    def __init__(self, f_name="firstname", l_name="lastname"):
        self.first_name = f_name # registering to self (instance attribute)
        self.last_name = l_name
    
    def __str__(self):
        return f"my name is {self.first_name} {self.last_name}"




john = Person("john", "doe")
print(john.country)
print(john.language)
print(john.__dict__) # all instce attributes
print(str(john)) # prints the object