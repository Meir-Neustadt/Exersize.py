import statistics
import re
import patterns
import func

class Member:

    count = 0

    def __init__(self, lname, fname, age, mail):
        self.lname=lname
        self.fname=fname
        self.age=age
        self.mail=mail
        Member.count+=1
    
    @property
    def lname(self):
        return self._lname
    @property
    def fname(self):
        return self._fname
    @property
    def age(self):
        return self._age
    @property
    def mail(self):
        return self._mail
    
    @lname.setter
    def lname(self, lname):
        if re.search(patterns.name_pattern, lname):
            self._lname=lname.capitalize()
        else:
            raise ValueError('not a valid last name')
    @fname.setter
    def fname(self, fname):
        if re.search(patterns.name_pattern, fname):
            self._fname=fname.capitalize()
        else:
            raise ValueError('not a valid first name')
    @age.setter
    def age(self, age):
        try:
            age=int(age)
        except:
            raise ValueError('not a number')
        if 16 < age < 120:
            self._age=age
        else:
            raise ValueError('not a valid age')
    @mail.setter
    def mail(self, mail):
        if re.search(patterns.mail_pattern, mail):
            self._mail=mail
        else:
            raise ValueError('not a valid mail')
        
    def __str__(self):
        return f'{self.lname} {self.fname}, {str(self.age)}, {self.mail},'
    

class Student(Member):

    def __init__(self, lname, fname, age, mail, grades):
        super().__init__(lname, fname, age, mail)
        self.grades=grades
        self.grade=grades

    @property 
    def grades(self):
        return self._grades
    @property 
    def grade(self):
        return self._grade

    @grades.setter
    def grades(self, grades):
        self._grades=grades
    @grade.setter
    def grade(self, grades):
        self._grade=func.ave(grades, 1)

    def __str__(self):
        return super().__str__() + f'{self.grades}, {self.grade}'



######################
    
student = Student('Meir','Neustadt',26,'msn.binah.1@gmail.com',[99,100,100,97,100,100,95,100,100,100,100])
print(student)
