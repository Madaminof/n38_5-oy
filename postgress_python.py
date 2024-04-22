"""
def tub_Count(list1: list[int]) -> int:
    result = 0
    for i in list1:
        c = 0
        for j in range(1, i + 1):
            if i % j == 0:
                c += 1
        if c == 2:
            result += 1
    return result
list1 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tub_Count(list1))"""


import psycopg2
from prettytable import PrettyTable
conn=psycopg2.connect(dbname='najottalim',host='localhost',port='5432',user='postgres',password='Samandar2004')
curr=conn.cursor()

def createTable(table_name):
    create_table_query = f'CREATE TABLE {table_name}(id SERIAL PRIMARY KEY, valyuta VARCHAR(10), miqdor INTEGER, uzs_som FLOAT)'
    try:
        curr.execute(create_table_query)
    except Exception:
        print("table mavjud")
    else:
        print("yaratildi")
createTable('kurs')    





def insert1(t_name):
    curr.execute(f"select *from {t_name}")
    c_name=[i[0] for i in curr.description]
    input_data=[input(f"{i} kirit = ") for i in c_name]
    curr.execute(f"insert into {t_name} values {tuple(input_data)}")
insert1("bugalter")    
    
