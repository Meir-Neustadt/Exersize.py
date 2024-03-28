import random
import re

list=[11, 22, 33, 44, 55, 66, 77, 88, 99]

random.shuffle(list)
list.insert(3,random.choice(list)+3)
num=list.pop()
if 22 in list:
    list.remove(22)
list.sort(reverse=True)

newList1=list[1:5:2]
newList2=[round(num/(num+20), 2) for num in list[:5]]

print(*list, sep='; ', end='.\n')
print(*newList1, sep=', ', end=':\n')
print(*newList2, sep=': ', end='|\n')

match list[3]:
    case 11:
        list[2]+=2
    case 22:
        list[4]+=200
    case _:
        list[1]-=100

while True:
    try:
        list.append(int(input('Enter a number: ')))
        break
    except:
        pass

altered = map(lambda n: n*2, list)
filtered = filter(lambda n: n%2==0, list)
sorted = sorted(list, key=lambda n: n//10)

print(*list)
print(*altered)
print(*filtered)
print(*sorted)

num=1234.56789
print(f"{round(num, 3):,}")