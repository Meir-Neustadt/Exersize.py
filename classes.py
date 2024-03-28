import re


class member:

    count = 0

    def __init__(self, lname, fname, age, mail: int):
        self.lname=lname
        self.fname=fname
        self.age=age
        self.mail=mail
        member.count+=1
    
    @property
    def lname(self):
        return self._lname
    @property
    def fname(self):
        return self._fname
    @property
    def age(self):
        return self._age
    
    @lname.setter
    def lname(self, lname):
        if re.search(r"^\w{3,20}$", lname):
            self._lname=lname.capitalize()
        else:
            raise ValueError('not valid last name')
    @fname.setter
    def fname(self, fname):
        if re.search(r"^\w{3,20}$", fname):
            self._fname=fname.capitalize()
        else:
            raise ValueError('not valid first name')
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
        
    def __str__(self):
        return(f'{self.lname} {self.fname}, {str(self.age)}')
    

class student(member):
    def __init__(self, lname, fname, age: int):
        super().__init__(lname, fname, age)

