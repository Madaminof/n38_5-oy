# Asinxron dasturlash-bu tizimni tez-tez 
# kuttirib turadigan og‘ir dasturlarni 
# optimallashtirish uchun juda kuchli vosita.

import asyncio  # asinxron kutubxonasi
"""
async def task1():
    print("1-Start")
    await asyncio.sleep(6)  
    print("1-finish")
    
async def task2():
    print("2-Start")
    await asyncio.sleep(7)
    print("2-finish")

async def result():
    await asyncio.gather(task1(),task2())
asyncio.run(result())    """


"""
import requests
url="https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
response=requests.get(url)
data=response.json()
#print(data[0])
type1=input("type")
type2=type1.upper()
miqdor=int(input("miqdor: "))
for i in data:
    if i['Ccy']==type2:
        print(f"{miqdor} {i["CcyNm_UZ"]}:{float(i["Rate"])*miqdor} som")
    """





#  1. https://cbu.uz/uz/arkhiv-kursov-valyut/json/   
#  shu malumotlarni malumotlar bazasiga yozing (asinxronda)
import psycopg2
from prettytable import PrettyTable
conn=psycopg2.connect(dbname='najottalim',host='localhost',port='5432',user='postgres',password='Samandar2004')
curr=conn.cursor()
'''
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
import requests
url="https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
response=requests.get(url)
data=response.json()
for i in range(1,len(data)):
    insert_data(data[i])'''


# 2. http://country.io/capital.json    shu malumotlarni malumotlar bazasiga yozing (asinxron)
'''
def createTable():
    try:
        create_table= """
    CREATE TABLE IF NOT EXISTS citys (
        country_code VARCHAR(2),
        city VARCHAR(100));
"""
        curr.execute(create_table)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error ", error)
    else:
        print("table yaratildi")    
#createTable()


def insert_data(data):
    try:
        insert_query ="INSERT INTO citys (country_code, city) VALUES (%s, %s)"
        insert=(data['country_code'],data['city'])
        curr.execute(insert_query,insert) 
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error", error)
    else:
        print("qoshildi")    
import requests
url="http://country.io/capital.json"
response=requests.get(url)
data=response.json()
for country_code, city in data.items():
    insert_data({'country_code': country_code, 'city': city})'''


# 3-masala

def count_narx(N):
    ways = [0] * (N + 1)
    ways[0] = 1
    
    for i in range(1, N + 1):
        if i >= 1:
            ways[i] += ways[i - 1]
        if i >= 2:
            ways[i] += ways[i - 2]
    
    return ways[N]

N = int(input("N somlik pul "))
print(f"{N} somlik pulni 1 somlik va 2 somlik pullar bilan {count_narx(N)} xil usulda tahlash mumkin.")

# 4-masala
def find_numbers(L, R, N):
    min_num = (N - R % N) + L if R % N < L % N else L
    max_num = R - (R % N) + (N - 1)
    return min_num, max_num
#print(find_numbers(1,20,5))

# 5-masala
def solution(numbers, target):
    a,b=0,0
    n = len(numbers)
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] + numbers[j] == target:
                a=i
                b=j
    return a,b
#print(solution([2,7,11,15],9)) 

# 6-masala           
def solution(s):
    n = len(s)
    if n == 0:
        return 0

    uzun = 1
    start = 0
    dic = {}

    for i in range(n):
        if s[i] in dic and start <= dic[s[i]]:
            start = dic[s[i]] + 1
        else:
            uzun = max(uzun, i - start + 1)
        dic[s[i]] = i
    return dic
#print(solution("bbbb"))

# 7-masala
def remov(nums):
    result = []
    while len(nums) > 0:
        if len(nums) >= 3:
            result.append(nums.pop(2))
        else:
            result.extend(nums[::-1])
            nums.clear()
    return result
nums = [10,20,30,40,50,60,70,80,90]
result = remov(nums)
print(result)

# 8-masala
def qavs(n):
    result = []
    def solution(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            solution(s + '(', left + 1, right)
        if right < left:
            solution(s + ')', left, right + 1)
    solution('', 0, 0)
    return result
n = 1
print(qavs(n))


# 9-masala
from itertools import product

def tel_harf_kambinatsiya(digits):
    if not digits:
        return []

    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    letters = [mapping[d] for d in digits]
    return [''.join(comb) for comb in product(*letters)]
print(tel_harf_kambinatsiya('23'))  



#10. Ikkita sonning EKUBini topuvchi dastur tuzing
def EKUB(a,b):
    a1=[]
    b1=[]
    lists=[]
    for i in range(1,a+1):
        if a%i==0:
            a1.append(i)
    for i in range(1,b+1):
        if b%i==0:
            b1.append(i)     
    for i in a1:
        if i in b1:
            lists.append(i)
    natija=max(lists)
    return natija        
print(EKUB(12,36))   


 # 11-misol   
def ekub(*args):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    result = args[0]
    for num in args[1:]:
        result = gcd(result, num)
    return result
print(ekub(24, 36, 48,12)) 




#12.  Kiritilgan sonning Palindrom yoki yo`qligini tekshiruvchi dastur yozing
def isPalindrome( x):
        s1=str(x)
        s2=s1[::-1]
        if s2==s1:
            return True
        else:
            return False    
print(isPalindrome(111))       

   


