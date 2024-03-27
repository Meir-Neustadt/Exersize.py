import random
import re

list=[11, 22, 33, 44, 55, 66, 77, 88, 99]
random.shuffle(list)
num=list.pop()
list.sort(reverse=True)
print(*list, sep=';', end=' ')
print() 

num=1234.56789
print(f"{round(num, 3):,}")