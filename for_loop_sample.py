#for loop-used to iterate over a sequence
"""my_list=[11,22,33,44,55,66]

for list in my_list:
    print(list,end="|")# end=" "  to print on the same line with space

print("")#used to print a blank line

my_tuple=(11,22,33,44,55,66)

for tuple in my_tuple:
    print(tuple,end="|")
print("")

my_set={11,22,33,44,55,3,"Ebin"}
print(my_set)

for set in my_set:
    print(set,end="|")

print("")

my_dict={"name":"man",11:11,"place":"earth"}
"""
"""for dict in my_dict:
    print(dict,end=":")
    print(my_dict,":",[dict])#shows both key and value.
print(my_dict.items())# .tems() used in dictionary.show key value pair as tuples.
for dict in my_dict.items():
    print(dict)
"""
"""for a,b in my_dict.items():
    print(a,":",b)#show both key and value.


my_newlist=["hi","hey","hello",1,2,3]
for l in enumerate(my_newlist):#enumerate used in sequences,default 0
    print(l)
print("")
for m in enumerate(my_newlist,6):#starts with 6
    print(m)"""


"""for even in range(1,11):
    if even%2==0:
        print(even,end=" ")"""

"""print("To find the sum of numbers from a starting number to ending number")
num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
total=0
for num in range(num1,num2+1):
    total+=num
print(f"sum of numbers from {num1} to {num2} is {total}")"""


"""print("to find how many vowels present in a word")
word=str(input("Enter the word :"))
vowels="aeiouAEIOU"
no_vowels=0
for a in word:
    if a in vowels:
        no_vowels+=1
print("number of vowels is :",no_vowels)"""

for num in range(1,11):
    if num==3:
        continue#
    print(num)
print("")
for num in range(1,11):
    if num==3:
        break
    print(num)