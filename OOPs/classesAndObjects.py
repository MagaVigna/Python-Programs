class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        print("Woof!")

dog1 = Dog("Fido", "Labrador")
print(dog1.name)  
print(dog1.breed)  
dog1.bark()  

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
        
#     def area(self):
#         return 3.14 * self.radius * self.radius
    
#     def circumference(self):
#         return 2 * 3.14 * self.radius

# circle1 = Circle(5)
# print(circle1.area()) 
# print(circle1.circumference())  

# class Student:
#     def __init__(self, name, age, grades):
#         self.name = name
#         self.age = age
#         self.grades = grades
        
#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)
    
# student1 = Student("Alice", 21, [80, 90, 95])
# student2 = Student("Bob", 19, [70, 80, 85])

# print(student1.name)  
# print(student1.average_grade())  
# print(student2.name)  
# print(student2.average_grade())  




