import random
import string

def ave (list, after_dot):
    return round(sum(list)/len(list), after_dot)

def print_list(rlist):
    list(map(print,rlist))

def random_name():
    return random.choice(string.ascii_lowercase)+random.choice(['a','i'])+random.choice(string.ascii_lowercase)+random.choice(['a','i'])

def random_mail():
    mail = ''.join(random.choice(string.ascii_lowercase) for _ in range(3)) + '@gmail.com'
    return mail

def random_grades():
    return [random.randint(45, 100) for _ in range(5)]