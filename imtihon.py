# 1-misol
import decimal
class ToDecima:
    def __init__(self,num):
        self.num=num
        
    def func(self,num):
        self.num=num
        decimal_num=decimal(num)
        return decimal_num
    
obj=ToDecima(12)
print(obj.num) 

# 2-misol
import psycopg2
import requests
conn=psycopg2.connect(dbname='najottalim',host='localhost',port='5432',user='postgres',password='Samandar2004')
curr=conn.cursor()

def create_table():
    try:
        create_table_query = """CREATE TABLE IF NOT EXISTS Product
               (id serial primary key,
               name varchar(64),
               price int,
               color varchar(64)); """
        curr.execute(create_table_query)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error ", error)
    else:
        print("table yaratildi")    
#create_table()

def insert_data(d):
    try:
        postgres_insert_query = """ INSERT INTO Product(id,name,price,color) VALUES (%s,%s,%s,%s)"""
        a=(d['id'],d['name'],d['price'],d['color'])
        curr.execute(postgres_insert_query,a)
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error", error)
    else:
        print("qoshildi")   
d={'id':1, 'name':'Samsung A72' , 'color':'black', 'price': 452.125478}
#insert_data(d)    

# 3-misol  git buyruqlaridan kamida 4 tasini yozing
'''
1. git init
2.git status
3. git add .
4. git commit -m ""
5. git push -u origin main

https://github.com/Madaminof/n38_5-oy
'''


# 4-misol
from collections import namedtuple

CAR=namedtuple("CARS",['model','color','price'])
class avto(CAR):
    def __new__(cls, model,color,price):
        return super(avto, cls).__new__(cls, model, color,price)

    def funk(self):
        return self.price*2
car1=avto('jentra','black',10000)
#print(car1.price) 
#print(car1.funk())  


# 5-misol
import psycopg2
def connect(user='postgres',dbname='najottalim',password='Samandar2004',host='localhost',port='5432'):
    def select():
        a1=user
        a2=dbname
        a3=password
        a4=host
        a5=port
        print(a1,' ',a2,' ',a3,' ',a4,' ',a5)
    return select    
closures=connect()
result=closures()
print(result)              

         


 
        

# 6-misol
class Alphabet:
    def __init__(self,lists):
        self.lists=lists
ob=Alphabet(['a','b','c','d','e'])
iter1=iter(ob.lists)
print(next(iter1))     
print(next(iter1)) 
print(next(iter1)) 
print(next(iter1)) 
print(next(iter1)) 




# 7-misol
keys = ["name", "description", "title", "keywords","content","charset"]
values = ["document","The best document","My document","doc, word,excel","None"]
result=zip(keys,values)
def generators(n):
    for i in n:
        yield i
#print(list(generators(result)))  
        



# 9-masala
"""
def create_table():
    try:
        create_table_query = '''CREATE TABLE IF NOT EXISTS product1
              (id serial primary key,
               title VARCHAR(100),
               description VARCHAR(100),
               price VARCHAR(100),
               discountPercentage VARCHAR(100),
                rating VARCHAR(100),
               stock varchar(100),
               brand varchar(100),
               category varchar(100),
               thumbnail varchar(100)


               

               ); '''
        curr.execute(create_table_query)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error ", error)
    else:
        print("table yaratildi")    
#create_table()

def insert_data(data):
    try:
        postgres_insert_query = ''' INSERT INTO produc(id, title, description,price,discountPercentage,rating, stock,brand,category,thumbnail) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        record_to_insert = (data['id'], data['title'], data['description'], data['price'],data['discountPercentage'],data['rating'],data['stock'],data['brand'],data['category'],data['thumbnail'])
        curr.execute(postgres_insert_query, record_to_insert)
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error", error)
    else:
        print("qoshildi")   

url="https://dummyjson.com/products"
response=requests.get(url)
data=response.json()
for i in range(len(data)):
    insert_data(data[i])

"""

# 10-masala
"""
import asyncio
url="https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
response=requests.get(url)
data=response.json()
async def result(d):
    await asyncio.sleep(1)
    print(d)
async def get_result():
     await asyncio.gather(result(data))
asyncio.run(get_result())    

    """
  













    
