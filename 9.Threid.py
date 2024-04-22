from asyncio import sleep
from multiprocessing import Pool
from time import time

from threading import Thread


#1. 4 ta ixtiyoriy funksiya yozing va ularni bir vaqtda ishlating(thread orqali) oddiy usulda va tread orqali ishlatib vaqtlar farqini chiqaring.
"""
def firstname():
    print("Samandar")
def lastname():
    print("madaminov")    

def salom():
    print("salom")
    sleep(3)
    print("hayir ")

def hello():
    print("hello")
    sleep(5)
    print("good bye ") 
# Thread funksiya
def Thread_time():
    start=time()
    t1=Thread(target=salom)
    t2=Thread(target=hello)
    t3=Thread(target=firstname)
    t4=Thread(target=lastname)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    stop=time()
    print("Thread",stop-start) 

# oddiy funksiya
def main_time():
    s=time()
    salom()
    hello()
    firstname()
    lastname()
    print("main",time()-s)
   
Thread_time()
main_time()   
"""

#2. sonlar toplami bor juflarini chiqaradigan funksiya yozing(funksiya 4 patokda ishlasin(Process))
def numbers(n):
    for i in range(len(n)):
        if n[i] % 2 == 0:
            print(n[i])

if __name__ == "__numbers__":
    start = time()
    with Pool(4) as p:
        n = [1, 2, 3, 4, 5, 6, 7, 8, 9,11,12,13,14]
        p.map(numbers, n)
    print(time() - start)



# 3-masala
"""def namesa(filename):
    with open(filename, 'r') as file:
        for line in file:
            name = line.strip()
            if name.startswith('a'):
                print(name)

if __name__ == "__main__":
    start = time()
    with Pool(3) as p:
        filename = "ism.txt"
        p.map(namesa, [filename])
    print(time() - start)"""


#4.Ismlar roxati bor uzunligi 5 dan katta bolgan ismlar oldidan False aks holda True yozib chiqarsin(3 patokda ishlasin)


def main(s):
    for i in s:
        if len(i)>5:
            print(False)
        else:
            print(True)    
           
if __name__=="__main__":
    start=time()
    with Pool(3) as p:
        s=["samandar","ali","valijon","dior"]
        p.map(main,s)
    print(time()-start)


# 5
def tub_murakkab(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num > 2 and num % 2 == 0:
        return False
    max_boluv = int(num ** 0.5) + 1
    for i in range(3, max_boluv, 2):
        if num % i == 0:
            return False
    return True

def sum_digits(num):
    return sum(int(digit) for digit in str(num))

def solution(num):
    digit_sum = sum_digits(num)
    result = "tub" if tub_murakkab(digit_sum) else "murakkab"
    print(f"{num}: {result}")

if __name__ == "__main__":
    start = time()
    with Pool(4) as p:
        numbers = [1,2,3,4,5,6,7]
        p.map(solution, numbers)
    print(time() - start)


#6.Sizga N ta nomanfiy butun sonlar beriladi, siz bu sonlarni kamaymaydigan tartibda saralab chop eting. 
def sortn(n):
    a=sorted(n)
    return a
n=[6,31415926535897932384626433832795,1,3,10,3,5]
print(sortn(n))

# 7-masalaa
"""def remove_duplikat(s):
    l = []
    for char in s:
        if l and l[-1] == char:
            l.pop()
        else:
            l.append(char)
    return ''.join(l) if l else 'Empty String'
input = [
    "aaabccddd",
    "aa",
    "baab"
]
for s in input:
    print(remove_duplikat(s))
"""

# masala8
def max_fun(n):
   l=[]
   a=0
   for i in range(1,n):
       if n%i==0:
           l.append(i)
   a=max(l)       
   return a        
n =12
print(max_fun(n))



"""
def main(s):
    s1=s.split()
    for i in s1:
        if len(i)>=5:
            print(True)
        else:
            print(False)    
           
if __name__=="__main__":
    start=time()
    with Pool(4) as p:
        s="Berilgan matndagi uzunligi" 
        p.map(main,s)
    print(time()-start)    
"""

        