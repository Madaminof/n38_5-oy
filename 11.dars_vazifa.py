# 1 Ikkita listning o'rta arifmetigini chiqaring.
l1=[1, 1, 3, 4, 4, 5, 6, 7]
l2=[0, 1, 2, 3, 4, 4, 5, 7, 8]
s1=sum(l1)
s2=sum(l2)
print((s1+s2)/(len(l1)+len(l2)))

#2:Listda nechta integer bor ekanligini aniqlovchi dastur tuzing.
def integer_num(n):
    c=0
    for i in n:
        if type(i) ==int:
            c+=1
    return c
l=[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
print(integer_num(l))   

# 3:Listdagi bo'sh tupplelarni o'chiruvchi dastur tuzing.
def tuple_remove(nums):
    result = [item for item in nums if item]
    return result
print(tuple_remove([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]))            

#4:Textdagi ma'lum belgini oxirgi uchragan indexini toping. Masalan:
def index_belgi(s,belgi):
    l=[]
    for i in range(len(s)):
        if s[i]==belgi:
            l.append(i)
    result=l[-1]
    return result
print(index_belgi("Hello, welcome to my world.",'o'))  


# 5-masala
def function(a,b):
    squares = []
    for i in range(a + 1, b):
        if (i ** 0.5) % 1 == 0:
            squares.append(i)
    return squares if squares else None
print(function(15,40))  


# 6: Ixtiyoriy fayl ichidagi eng uzun so'zni aniqlovchi dastur tuzing
def length_soz():
    with open("ism.txt","r") as a:
        for i in a.readlines():
            a=i.split()
    b=max(a)
    return b         
print(length_soz())     



# 7
def count_lines(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)
print(count_lines("ism.txt"))

   

#8
def is_palindrome(number):
    num_str = str(number)
    reversed_num = num_str[::-1]
    return num_str == reversed_num

test_cases = [1111, 1011, 9696]

for i, num in enumerate(test_cases, start=1):
    result = "YES" if is_palindrome(num) else "NO"
    print(f"{i}\t{num}")
    print(result)



            

