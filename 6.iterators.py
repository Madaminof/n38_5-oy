
"1-masala"
def lists(l1,l2):
    a=0
    orta_arif=0
    s=0
    l3=l1+l2
    for i in l3:
        if l3.count(i)==1:
            s+=i
            a+=1
    orta_arif=s/a
    return orta_arif  
print(lists([1, 1, 3, 4, 4, 5, 6, 7],[0, 1, 2, 3, 4, 4, 5, 7, 8]))


# 2-masala
def add_front(n,nums):
    l1=[]
    for i in nums:
        l1.append(n+str(i))
    return l1
print(add_front("Rm",[1, 4, 3, 9]))

# 3-masala
def list_sum_max(lists1):
    l5=[]
    for i in lists1:
        a=sum(i)
        l5.append(a)    
    return max(l5)
print(list_sum_max([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]))   


# 4-masala
def integer_lists(l):
    s=0
    for i in l:
        if type(i)==int:
            s+=1
    return s
print(integer_lists([1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]))  


# 5-masala
def max_duplicate(lst):
    max_count = 0
    result = 0
    for i in lst:
        count = lst.count(i)
        if count > max_count:
            max_count = count
            result = i
    print(str(result) + " -> " + str(max_count) + " marta")
max_duplicate([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2])

# 6-masala
# [1,2,3]
def num(nums):
    s1=""
    l=[]
    for i in nums:
        s1+=str(i)
    number=int(s1)+1
    s2=str(number)
    for i in s2:
        l.append(int(i))
    return l
print(num([1,2,3]))    


# 7-masala
"""def Nums_kvadrat(n):
    l=[]
    l1=[]
    for i in range(n):
        l.append(int(input(f"{i+1}- sonni kiriting: ")))
    for i in l:
        l1.append(i**2)
    return l1 
print(Nums_kvadrat(5))   """

# 8-masala
def merge_lists(lst1, lst2):
    list1 = []
    for i in range(min(len(lst1), len(lst2))):
        list1.append(lst2[i] + str(lst1[i]))
    return list1
lst1 = [1, 4, 3, 9]
lst2 = ['chelsea', 'real', 'barca', 'MU']
print(merge_lists(lst1, lst2)) 


# 9-masala
def listss(l1,l2):
    elements = []
    for i in l1:
        if i in l2:
            elements.append(i)
    return elements
print(listss([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])) 


# 10-masala
def fib(n):
    a=0
    b=1
    l=[]
    l1=[]
    l.append(a)
    l.append(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        l.append(b)
    set1=set(l) 
    list1=list(set1)   
    for i in list1:
        if i>=1 and i<=n:
            l1.append(i)        
    return l1  
print(fib(7))





