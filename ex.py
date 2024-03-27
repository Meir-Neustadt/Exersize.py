import random
import re

list=[11, 22, 33, 44, 55, 66, 77, 88, 99]

random.shuffle(list)
num=list.pop()
if 22 in list:
    list.remove(22)
list.sort(reverse=True)

newList1=list[1:5:2]
newList2=[round(num/(num+20), 2) for num in list[:5]]

print(*list, sep='; ', end='.\n')
print(*newList1, sep=', ', end=':\n')
print(*newList2, sep=': ', end='|\n')

num=1234.56789
print(f"{round(num, 3):,}")