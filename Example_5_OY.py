# postgres TO python
'''import psycopg2
import requests
conn=psycopg2.connect(dbname='najottalim',host='localhost',port='5432',user='postgres',password='Samandar2004')
curr=conn.cursor()

def create_table():
    try:
        create_table_query = """CREATE TABLE IF NOT EXISTS valyuta
              (ID SERIAL PRIMARY KEY,
               Code VARCHAR(10),
               Ccy VARCHAR(10),
               CcyNm_RU VARCHAR(100),
               CcyNm_UZ VARCHAR(100),
               CcyNm_UZC VARCHAR(100),
               CcyNm_EN VARCHAR(100),
               Nominal VARCHAR(100),
               Rate VARCHAR(100),
               Diff VARCHAR(100),
               Date VARCHAR(64)); """
        curr.execute(create_table_query)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error ", error)
    else:
        print("table yaratildi")    
#create_table()

def insert_data(data):
    try:
        postgres_insert_query = """ INSERT INTO valyuta(id, code, ccy, ccynm_ru, ccynm_uz, ccynm_uzc, ccynm_en, nominal, rate, diff, date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (data['id'], data['Code'], data['Ccy'], data['CcyNm_RU'], data['CcyNm_UZ'], data['CcyNm_UZC'], data['CcyNm_EN'], data['Nominal'], data['Rate'], data['Diff'], data['Date'])
        curr.execute(postgres_insert_query, record_to_insert)

        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error", error)
    else:
        print("qoshildi")   

url="https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
response=requests.get(url)
data=response.json()
for i in range(1,len(data)):
    insert_data(data[i])
'''

# NameTuple
from collections import namedtuple
"""
CAR=namedtuple("CARS",['model','color','price','year'])
dic={}
bmw1=CAR('BMW M8','black',80000,2024)
bmw2=CAR('BMW M4','blue',60000,2021)
"""

# clolures ichma ich funksiya
"""def outer_functopn(x):
    l=[]
    def inner_function(y):
        nonlocal l
        l=[]
        for i in range(x,y+1):
            l.append(i**2)
        return l
    return inner_function
closure=outer_functopn(2)  
result=closure(20)
print(result)"""


# Sequense TYPES
"""l1=['green','blue','red','orange','yellow']
print(l1[2:3])
print(l1[:1])"""


# iterators
l1=['green','blue','red','orange','yellow']
iter1=iter(l1)
"""print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))"""
'''for i in l1:
    print(next(iter1))'''

# GENERATORS (yield)
"""def solution(n):
    for i in range(1,n+1):
        yield i**2
print(list(solution(10)))   

def fibonacci(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
        yield a
print(list(fibonacci(10)))    

"""


# MULTI THREID 
'''from threading import Thread
from time import time
def kvadrat():
    l1=[]
    for i in range(1,10):
        l1.append(i**2)
    print(l1)


def kub():
    l=[]
    for i in range(1,10):
        l.append(i)
    print(l)
def Threid_func():
    start=time()
    t1=Thread(target=kvadrat)
    t2=Thread(target=kub)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    stop=time()
    print("Threid",stop-start)
Threid_func()
'''
# Multi prosessing
from multiprocessing import Pool,Process
from time import time
"""def func(x):
    return x*x
if __name__=='__main__':
    start= time()
    with Pool(4) as p:
        print(p.map(func,[1,2,3,4]))
    stop=time()
    print(stop-start)
def get_name(name):
    print(f"hello {name}")
if __name__=='__main__':
    start=time()
    pr1=Process(target=get_name,args=('Tony',))
    pr1.start()
    pr1.join()
    stop=time()
    print(stop-start)
"""

# Asincron va sinxron
import asyncio
"""
# tanishuv chati tuzamiz
shaxs=namedtuple("shaxs",['name','age','addres'])
shaxs1=shaxs('john',19,'newyork')
shaxs12=shaxs('tony',23,'tokio')

async def Tanishuv():

    print(f"SHaxs1: Salom meni ismim {shaxs1.name}")
    await asyncio.sleep(2)
    print("Shaxs1: sizning ismingiz nima")
    start = time()
    await asyncio.sleep(10)
    stop=time()
    if (stop-start)>5:
        print("sizni javobingizni kutyapman")
    else:
        print("uzur ozgina kechikdim.")
        print(f"SHaxs2: Salom meni ismim {shaxs12.name}")
asyncio.run(Tanishuv())
"""

"""async def get_name():
    await asyncio.sleep(2)
    print(f"name - tony")
async def get_age():
    await asyncio.sleep(4)
    print(f"age - {20}")

async def main():
    await asyncio.gather(get_name(),get_age())
asyncio.run(main())
"""












        


import requests  
url="https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
response=requests.get(url)
data=response.json()
for i in data:
    for j in i:
        print(j)
    break    











