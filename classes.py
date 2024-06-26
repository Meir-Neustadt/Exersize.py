import re
import random
import patterns
import func as f

class Member:

    _count = 0

    def __init__(self, lname, fname, age, mail):
        self.lname=lname
        self.fname=fname
        self.age=age
        self.mail=mail
        Member._count+=1

    @classmethod
    def count(cls):
        return cls._count 
    
    @property
    def lname(self):
        return self._lname
    @property
    def fname(self):
        return self._fname
    @property
    def name(self):
        return f'{self._fname} {self.lname}'
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
        if 14 < age < 120:
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
        return f'\n{self.name}, {str(self.age)}, {self.mail},'
    

class Student(Member):

    _students = []

    def __init__(self, lname, fname, age, mail, grades):
        super().__init__(lname, fname, age, mail)
        self.grades=grades
        self.grade=grades
        Student._students.append(self)

    @classmethod
    def students(cls):
        return cls._students
    @classmethod
    def exelent_students(cls):
        students = cls.students()
        students = filter(lambda st: st.grade > 85, students)
        return students

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
        self._grade=f.ave(grades, 1)

    def __str__(self):
        return super().__str__() + f'\ngrades: {self.grades}, average: {self.grade}'



######################
    
student1 = Student('Neustadt','Meir',26,'msn.binah.1@gmail.com',[99,100,100,97,100,100,95,100,100,100,100])
students_list = [Student(f.random_name(), f.random_name(), random.randint(15,60), f.random_mail(), f.random_grades()) for _ in range(20)]

f.print_list(Student.exelent_students())
