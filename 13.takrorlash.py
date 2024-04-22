# 1-NamedTaple
"""
from collections import namedtuple
#bu clasga oxshash funksiya
student=namedtuple('Student',['name','age','addres'])
# obekt yaratamz
s1=student('Samandar',19,'Qoqon')
print(s1.age)
print(s1[0])

"""
# Closures ichma ich funksiya
"""def greet(name):
    def display_name():
        print("Hi", name)
    display_name()
greet("John")  """

def cal():
    n=1
    def num():
        nonlocal n
        n+=2
        return n
    return num
a=cal()
print(a())  
print(a())  
print(a())  








# 2-Sequence types











# 3-Iterators
# Python iterator ob'ekti ikkita maxsus usulni amalga oshirishi kerak
# __iter__() va __next__()birgalikda iterator protokoli deb ataladi.

# oddiy for loop da iteratorni ishlatamiz
"""lists=[3,5,8,2,94,1]
for i in lists:
    print(i)"""

# iter() funksiyasida koramiz
"""
lists=[3,5,8,2,94,1]
iterator=iter(lists)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
"""

# Infinite(cheksiz) Iterators
from itertools import count

cheksiz_iter=count(100)
for i in range(5):
    print(next(cheksiz_iter))


class Square:
    def __init__(self,color):
        self.color=color
        self.number=0
        self.l=[]

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.color)<=self.number:
            raise StopIteration
        
        self.number+=1
        self.l.append(self.number)
        self.result=zip(self.color,self.l)

        return list(self.result)
      

obekt1=Square(['green','reed','orange','blue'])
"""print(next(obekt1))
print(next(obekt1))
print(next(obekt1))
print(next(obekt1))"""
for i in obekt1:
    print(i[-1])



   





  












# 4 Generators
# Generator - bu Yield kalit so'zidan foydalangan holda iteratorni qaytaradigan funksiya.

# example_1
"""
def generator1():
    for i in range(1,10):
        yield i
for i in generator1():
    print(i)    
"""

# example_2
"""def fib(n):
    try:
        a,b=0,1
        while a<n:
            yield a
            a,b=b,a+b
    except StopIteration:
        print(f"ptint {n} dan oshib ketmasin!")
    else:
        print("dastur ishladi")    
x=fib(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))"""


l=[1,2,3,4,5,6,7,8]
dict1={}
for i in l:
    if i%2==0:
        dict1[i]=True
    else:
        dict1[i]=False
print(dict1)        












# Context manager
with open('data.txt') as f:
    data = f.readlines()
    print(int(data[0]))




