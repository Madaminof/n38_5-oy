# mavzu: Closures
# funksiya ichida funksiya ishlatish
# obekt qaytaradi
"""def a():
    b=1
    def inner():
        print(b)
    return inner
print(a())    
"""
# ozgaruvchiga olib chiqarsak obekt qaytarmaydi
"""def a():
    b=1
    def inner():
        print(b)
    return inner
func=a()
func()   
l1=[1,2,3,4,5,6,7,8,9]
l2=["john","tom","tommy"]"""



from collections import namedtuple

# 1.nameTaple ga misol
Poind2D=namedtuple("Poind2D",('x','y'))
point1=Poind2D(200,300)
def Max():
    if point1.x>point1.y:
        print(point1.x)
    else:
        print(point1.y)    
Max()        
#print(point1.x)
#print(point1.y)

# 2.nameTaple ga misol
Student=namedtuple("Student",("name","age","addres")) # class yaratildi
S1=Student("Tony",20,"New York")   # obekt yaratildi
S2=Student("John",17,"Pentagon")   # obekt yaratildi
def Age_20():
    if S1.age==20:
        print(S1.name,S1.age,S1.addres)
    elif S2.age==20:
        print(S2.name,S2.age,S2.addres)    
    else:
        print("bunday yoshli student yoq")    
Age_20()        


# 3.nameTaple ga misol
Cars=namedtuple("cars",("model","color","price"))
car1=Cars("BMW M5","Black",50000)
car2=Cars("Mers","Blue",45000)
car3=Cars("BYD","Black",30000)

def Color_Black_Count():
    c=0
    l=[]
    l.append(car1.color)
    l.append(car2.color)
    l.append(car3.color)
    for i in l:
        if i=="Black":
            c+=1
    return c        
print(Color_Black_Count())   


# 4.nameTaple ga misol
Phones=namedtuple("Phone",("model","color","storage","price"))
phone1=Phones("iphone 13","Black","128Gb",600)
phone2=Phones("samsung S21","Blue","512Gb",900)
phone3=Phones("redmi not12","White","256Gb",400)

def Price_500_katta_name():
    l1=[]
    if phone1.price>=500:
        l1.append(phone1.model)
    elif  phone2.price>=500:
        l1.append(phone2.model)   
    elif phone3.price>=500:
        l1.append(phone3.model)   
    return l1 
print(Price_500_katta_name())  

print(phone1.model)



#  NamedTuple ni boshqa classga vorislik qilib berish
Person = namedtuple('Person', ['name', 'age',"addres"])
class Shaxs:
    def __init__(self, person: Person, position: str):
        self.person = person
        self.position = position
person_info = Person(name='Ali', age=30,addres="new york")
shaxs = Shaxs(person=person_info, position='Developer')

print(shaxs.person.name)  # Ali
print(shaxs.person.age)   # 30
print(shaxs.position)     # web developer




# fayldagi masalalar
# 1-masala
def yolgiz_Son(nums):
    for i in nums:
        if nums.count(i)==1:
            return i
print(yolgiz_Son([1,2,3,4,3,2,1]))    


# 2-masala
def dasturchilar_kuni(yil):
    dasturchilar_kuni_boshlanishi = (255, 9, yil) 
    kabisa_yil = (yil % 400 == 0) or ((yil % 4 == 0) and (yil % 100 != 0))    
    if kabisa_yil:
        dasturchilar_kuni = 12
    else:
        dasturchilar_kuni = 13
    return f"{dasturchilar_kuni}/{dasturchilar_kuni_boshlanishi[1]}/{dasturchilar_kuni_boshlanishi[2]}"
print(dasturchilar_kuni(2000)) 



# 3-masala
def Parta(a,b,c):
    return int(((a+b+c)+1)//2)
print(Parta(20,21,22))





