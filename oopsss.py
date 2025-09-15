# 11-09-2025
# self it refrece TO working on
# construter - spl type of method 
# cont = __inti__
# Types of variables -- to store are 2 types
# instance varibales and class/static variable
# 3 types of methods-Instance methods,class methods, static methods ---- here class and static are diffrennt


# instance variabele- any variable whose value  is depends on a object(instances) 
# class/static = object unna lekunaa value chepachu --- okate 
# you dont say  
# exmple mahandea cars company 



# methodes- 3methods
# instance-any method  is any class methods which have one atleast instance variable inside in it
# class method - in this type of methods we use class or static method(static lo class and ojecct use cheyaradhu) - no need instances(object
# @classmethod #(dectorector)
# def change_company_name(cls,new_comp_name): # genral ga cls anipedutham
#     cls.company_name = new_comp_name

# @staticmethod
# def connect_to_databse(db_username.db_password):
    # num1 = 10+20
#########################################################################################################33*...........................................
class Student:
    def __init__(self, name, age):
        # Instance Variables
        self.name = name
        self.age = age

    # Instance Method
    def show_details(self):
        print("Name:", self.name, "| Age:", self.age)

    # Another Instance Method
    def birthday(self):
        self.age += 1
        print(self.name, "is now", self.age, "years old!")


# Create objects
s1 = Student("Riya", 20)
s2 = Student("Arjun", 22)

# Access Instance Variables
print(s1.name)   # Output: Riya
print(s2.age)    # Output: 22

# Call Instance Methods
s1.show_details()   # Output: Name: Riya | Age: 20
s1.birthday()       # Output: Arjun is now 23 years old!




# Instance variables → store data unique to each object (self.name, self.age).
# Instance methods → perform actions using that object’s data (show_details, birthday).
###############################################
# Real-life Analogy (Car Example)
class Car:
    def __init__(self, brand, color):
        # Instance Variables
        self.brand = brand
        self.color = color

    # Instance Method
    def show_car(self):
        print("Car:", self.brand, "| Color:", self.color)

    # Another Instance Method
    def repaint(self, new_color):
        self.color = new_color
        print("The car has been repainted to", self.color)


# Create Car objects
c1 = Car("BMW", "Red")
c2 = Car("Tesla", "Black")

# Access Instance Variables
print(c1.brand)   # Output: BMW
print(c2.color)   # Output: Black

# Call Instance Methods
c1.show_car()     # Output: Car: BMW | Color: Red
c2.repaint("Blue") # Output: The car has been repainted to Blue
    

# Instance variables → brand, color (each car has its own).
# Instance methods → show_car(), repaint() (actions that car can perform).

############################################################################################################33........................................


# #######################Inheritance
# Parent class
class Animal:
    def sound(self):
        print("Animals make sounds")

# Child class
class Dog(Animal):   # Dog inherits from Animal
    def bark(self):
        print("Dog barks: Woof Woof")

# Create object of Dog
d = Dog()
d.sound()   # Inherited from Animal
d.bark()    # Defined in Dog
# output
# Animals make sounds
# Dog barks: Woof Woof


################################################3

# What is Single Inheritance?
# Inheritance means one class (child) can reuse the code of another class (parent).
# Single Inheritance = when a class inherits from only one parent class.
# Helps in code reusability and avoiding repetition.
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")

# Child Class (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print(self.name, "is barking")

# Create object of Dog (child class)
d = Dog("Tommy")

# Access parent class method
d.eat()    # Output: Tommy is eating

# Access child class method
d.bark()   # Output: Tommy is barking

# 🔹 Explanation
# Animal → Parent class (base class).
# Dog → Child class (derived class).
# Dog inherits eat() method from Animal.
# Dog also has its own method bark().
######################################################3
# Real-life Analogy (Car Example)

# Parent class
class Vehicle:
    def start(self):
        print("Vehicle is starting")

# Child class
class Car(Vehicle):
    def drive(self):
        print("Car is driving")

# Object of Car
c = Car()
c.start()   # Inherited from Vehicle → Vehicle is starting
c.drive()   # Defined in Car → Car is driving


#######################################