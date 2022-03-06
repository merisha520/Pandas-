class Student(object):
    '''This is a student class that has a constructor and attributes names and gpa. 
    It also has a class variable count and a static method get_count that counts the number of instances of the class.
    It has a get_standing class that gives the standing of the instances of the class'''
    
    count = 0 
    #creating costructor
    def __init__(self, name, gpa):
        self.name = name
        self.gpa= gpa
        Student.count +=1 

    '''def __str__(self):
        temp = 'Student with name :' + self.name + ' has a standing of ' + self.get_standing()
        return temp'''

        
    #creating get_standing method
    def get_standing(self):
        if self.gpa > 3:
            GPA = 'A'
        elif self.gpa >2 and self.gpa <3: 
            GPA = 'B'
        else:
            GPA = 'C'
        return GPA
#creating static method get_count
    @staticmethod
    def get_count():
        return Student.count
    
#instantiating two objects of Student class
Student1 = Student('John', 3.65)
Student2 = Student('Peter', 2.67)

#call get_standing methods on each of the instances
print(Student1.get_standing())
print(Student2.get_standing())  

#call get_count method on each of the instances
print(Student1.get_count())
print(Student2.get_count())



    
    