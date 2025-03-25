import json
class Person:
    gender = "Female"
    id_number = "test_id"
    def __init__(self, f_name, l_name, age):
        self.firstname = f_name
        self.lastname = l_name
        self.age = age
    
    def __str__(self):
        name =  self.full_name()
        return name
    
    def full_name(self):
        return self.firstname + " " + self.lastname


class Employee(Person):
    def __init__(self,f_name, l_name, age, job, pay):
        #try using super
        super().__init__(f_name, l_name, age)
        self.job = job
        self.pay = pay
    
    def give_raise(self, bonus=0):
        self.pay += bonus


class Files:
    def __init__(self, filename: str):
        self.filename = filename
    
    def read(self):
        print("reading file")
    
    def write(self, to_filename:str):
        print("writing to file")
    
    def update(self, to_filename:str):
        print("updating file")

class JsonFiles(Files):
    def read(self):
        with open(self.filename) as json_file:
            data = json.load(json_file)
            print(data)   
    def write(self, to_filename:str, dict_obj):
        with open(to_filename , "w") as json_file:
            json.dump(dict_obj, json_file)
    
    def update(self, to_filename:str):
        print("updating file")

jane = Employee("jane", "doe", 34, "cleaner", 30000)
json_object = JsonFiles("test_file.json")
data = jane.__dict__
json_object.write("export_file.json", data)