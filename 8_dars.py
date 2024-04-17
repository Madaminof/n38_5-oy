#1.Vaqtlar oralig'i
import math
def Time2(a,b):
    sek=0
    hour=abs(a-b)
    sek=hour*3600
    return sek
print(Time2(5,7))

# 2-masala
def JuftBoluv(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i
juft=list(JuftBoluv(10))
print(juft)   

# 3.Berilgan songacha bolgan tup sonlarni chiqaradigan generator yozing
def TubN(n):
    for i in range(1,n+1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            yield i        
result=list(TubN(7))            
print(result)    


#4.berilgan sonning tub boluvchilarini chiqaring generator orqali 
def Tub_boluvchilari(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    for i in range(1,len(l)):
        c=0
        for j in range(1,i+1):
            if l[i]%j==0:
                c+=1
        if c==1:
            yield l[i]
result=list(Tub_boluvchilari(8))
print(result)        


# 5-masala
def generatsiya_juft(sonlar):
    for son in sonlar:
        if son % 2 == 0:
            yield son
sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
generator = list(generatsiya_juft(sonlar))
print(generator)

#6.Berilgan bir matndagi so'zlar ketma-ketligini o'qib, har bir so'zning uzunligini generatsiya qiluvchi funksiya yozing.
def Text_length(s):
    s1=s.split()
    for i in s1:
        yield len(i)
s="Berilgan bir matndagi so'zlar ketma-ketligini o'qib, har bir so'zning uzunligini generatsiya qiluvchi funksiya yozing"        
result=list(Text_length(s))       
print(result) 



# 7.Berilgan matndagi uzunligi 5 dan katta bolgan sozlarni qaytaradigan generator yozing
def Text_len_5(s):
    s1=s.split()
    for i in s1:
        if len(i)<=5:
            yield i
s="Berilgan matndagi uzunligi 5 dan katta bolgan sozlarni qaytaradigan generator yozing"            
result=list(Text_len_5(s))
print(result)




# 8.Berilgan roxatda 3 marta qatnashgan sonlarni qaytaradigan generator yozing
def lists(l):
    for i in l:
        if l.count(i)==3:
            yield i
l=["abs","abs","abs","cieudc","a","a","a"]    
r=set(lists(l))
print(list(r))        

       







