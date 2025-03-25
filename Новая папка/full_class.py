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
    
    # def change_gender(self, gender):
    #     self.gender = gender
        


# class Manager(Employee):
#     pass

angella = Person("Angella", "Doe", 67)
print(angella.gender)
print(angella.firstname)
print(angella.full_name())
print(angella)

jonathan = Employee("Jonathan", "doe", 30, "python dev", 40000)
jonathan.gender = "Male"
print(jonathan.gender)
print(jonathan.firstname)
print(jonathan.lastname)
print(jonathan)
print(jonathan.pay)
jonathan.give_raise(800)
print(jonathan.pay)

alice = Employee("alice", "doe", 40, "java dev", 10000)
print(f"alice gender {alice.gender}")