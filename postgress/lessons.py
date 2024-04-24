import psycopg2

conn=psycopg2.connect(dbname='darsliklar',host='localhost',port='5432',user='postgres',password='Samandar2004')
cur=conn.cursor()


def create_table():
    try:
        query='''CREATE TABLE mavzular(
            id bigserial PRIMARY KEY,
            lesson_Name VARCHAR(64),
            txt TEXT
            );'''
        cur.execute(query)
        conn.commit()

    except Exception:
        print("error")
    else:
        print("table yaratildi")
#create_table()
dict1 = {
    'NamedTuple': 'namedtuple, Pythonning collections modulida joylashgan kutilgan qisqichbaqiy malumot strukturasidir. U, ozida koplab qiymatlarni saqlay olgan va unga atamalangan atributlarni (nomlarni) bor bolgan obyekt yaratadi.',
    'Iterator': 'Iterator, Python dasturlash tilida kop qollaniladigan obyekt bolib, oddiyroq deyish mumkin. Asosiy vazifasi, malum bir qatorni korib chiqish imkonini berishdir. Iteratorlar, __iter__() va __next__() metodlari orqali bajariladi.',
    'Generator': 'Asosiy vazifasi, malum bir qatorni generatsiya qilish va uni oz ichiga oluvchilar orqali chaqirishni boshqarishdir Generatorlar, fonksiyonlarga oxshash bolib, (yield) ifodasini ishlatib malumot qaytaradi. Buning natijasida, funksiya bajarilganda ozida biror qayta kirish nuqtasi saqlanadi.Generatorlar ham iteratorlar bilan bir xil ravishda ishlaydi va bu, ulardan turli xil foydalanishga imkon beradi. Ularning asosiy afzalliklari:',
    'Thread': 'Parallelism: Thread, kodni bir nechta joyda bir vaqtda bajarish imkonini beradi. Bu, masalan, dasturni ishga tushirish orqali vaqt va resurslardan tejashga yordam beradi.Concurrency: Concurrency, bir nechta amalni bir vaqtda bajarishning yana bir usuli hisoblanadi. Threadlar, bitta dastur ichida bir nechta amalni parallel bajarishga imkon berad'
}

"""def insert(data):
    try:
        query = '''INSERT INTO mavzular(lesson_name, txt) VALUES(%s, %s)'''
        for key, value in data.items():
            a = (key, value)
            cur.execute(query, a)
        conn.commit()
    except Exception as e:
        print("Error:", e)
    else:
        print("Inserted successfully")
"""
#insert(dict1)
