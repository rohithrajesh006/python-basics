
#sum of even numbers in a list
"""my_list=[1,2,3,4,5,6,7,8,9,10]
total=0
for num in my_list:
    if num%2==0:
        total+=num
        print(total)

name="athul"
print(name[::-1])


for a in range(1,5):
    print("*",end="")
for b in range(1,4):
    print("*   *")
for c in range(1,6):
    print("*",end="")
print()"""

"""while True:
 try:
    a,b=map(int,input("Enter two numbers:").split())
    try:
        c=a/b
        print(f"{a}/{b}={c}")
    except ZeroDivisionError:
        print("Zero division error")
    except NameError:
        print("value not defined")
    except Exception as e:
        print(e,"error")
 except ValueError:
     print("invalid literal")
 else:
     print("good, no errors")
     break
 finally:
     print("program executed")
"""

"""n=int(input("Enter a number :"))
if n%2==0:
    
        if  2<=n<=5:
         print("Not Weird")
        elif 6<=n<=20:
         print("Wierd")
        elif n>20:
         print("Not weird")
else:
        print("Weird")"""

"""def is_leap(year):
    
    
    # Write your logic here
    if (year%4==0 and year%100!=0 )or year%400==0:
        return True
    
    else:
        return False

year = int(input())
print(is_leap(year))"""

"""N=int(input("enter an odd number:"))
M=N*3
for a in range(N):
    print(".|."*a)"""


"""x = int(input("x--"))
y = int(input("y--"))
z = int(input("z--"))
n = int(input("n--"))
list=[[i,j,k]
    for i in range(0,x+1)
    for j in range(0,y+1)
    for k in range(0,z+1)
    if i+j+k!=n]
print(list)"""


"""sum=0
for i in range(1,11):
    sum+=i
print(sum)"""


"""number=[1,2,3,4,5]
even_number=[ num for num in number if num%2==0]
print(even_number)"""

"""for i in range(1,6):
    for k in range(1,11):
        mul=i*k
        print(f"{i} x {k} = {mul}",end="      ")
    print()
"""

"""password = ""
while password != "python123":
    password = input("Enter password: ")
else:
    print("Correct password!")"""

"""numbers=[1,2,3,4,5]
target=int(input("enter the target number:"))
for num in numbers:
    if num==target:
        print("Number found")
        break
else:
        print("Number not found")"""
"""while True:
    number=int(input("Guess a number:"))
    target=6
    if number==target:
     print("correct Guess")
     break
    else:
     print("Try again")
              """

"""for i in range(1,5):
    for j in range(1,7):
        print("*",end=" ")
    print()"""

"""for i in range(5):
   for j in range(5):
     if i == 0 or i == 4 or j == 0 or j == 4:
         print("*", end=" ")
     else: print(" ", end=" ")
print()"""

"""for i in range(5, 0, -1):
     for j in range(1, i + 1):
         print(j, end=" ")
     print()"""

