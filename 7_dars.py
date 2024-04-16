# 1-misol
dic={
    "1":11,
    "2":2,
    "3":44,
    "4":1
}
sort_dict=sorted(dic.values(),reverse=False)
#print(sort_dict)



#2-misol
"""dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)"""
#print(dic1)
"""
# 3-masala
def dictFunction(n):
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    return d
#print(dictFunction(5))    


# 4. dict ning valuelari yig`indisini toping.
def dict_Values_Sum(dict1):
    s=0
    for i in dict1.values():
        s+=i
    return s
d={1:3,
   3:5}
print(dict_Values_Sum(d))    


# 5. dict ning valuelari orasidagi eng katta sonni toping.
dic1={1:10, 2:20,5:5}
def Max_dict_values(d):
    return max(d.values())
print(Max_dict_values(dic1))

def Min_Values(d):
    return min(d.values())
print(Min_Values(dic1))

"""

# 7-masala
"""
def merge_dicts(d1, d2):
    result = {}
    for key, value in d1.items():
        result[key] = value
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

merged_dict = merge_dicts(d1, d2)
print(merged_dict)"""


"""
l=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
result=[]
for i in l:
   for j in i.values():
       result.append(j)
for i in result:
    if result.count(i)==1:
        print(i)   """


"""
def Soz_count(a):
    for i in a:
        b=a.count(i) 
        print(i," ",b," ta")   
Soz_count('assalom')     """ 

"""
s='mexaniazasiyalashtirilganmi'
a=[]
d={}
d1={}
for i in s:
    a.append(s.count(i))
    b=max(a)
    if b==s.count(i):
        d[i]=s.count(i)
for i,j in d.items():         
    if j==b:
        d1[i]=j        
print(d1)    """
"""
d={""}
s='mexanizasiyalashtirilganmi'
a=[]
d={}
for i in s:
    a.append(s.count(i))
    b=max(a)
    if b==s.count(i):
        d[i]=s.count(i)

print(d)    """

"""
import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)"""


"""
a=("john","charles","mike")
b=("jenny","christy","monica","jonny")
s=list(zip(a,b))

def object(obj):
    for i in obj:
        yield i
h=object(s)     
print(next(h))
"""
"""
def fib(n):
    s=0
    for i in range(n-2,n):
       s+=i
    return s   
print(fib(5))"""




