#numbers(int,float,complex)

#integer-int
num=10
print(type(num))

#floating point-float
num1=3.14
print(type(num1))

#complex numbers-complex
a=2j
print(type(a))

#sequence datatypes(string,list,tuple)

#string()  immutable,string values must be in "" or ''
language="python"
print(type(language))
print(language[3])#to access h 

#list[] ordered,mutable
my_list=["python","java",1,23,[6,"one team"]]
#           0        1   2  3       4
print(type(my_list))
print(my_list[4][1])#accesing elements in list (inside list)using index numbers(mutable)
my_list[1]="c"#in list we can change the elements by (variable_name[position]=new element to assign)
print(my_list)


#tuple ()  ordered
my_tuple=("hi","hello",2,5,("heyy","you"))
print(type(my_tuple))
print(my_tuple)
print(my_tuple[4][0])
#my_tuple[2]=8 here we cannot change in tuple like in list(immutable)


#set{}  unordered(changes the order of elements every time we run the code)no repetition
my_set={"hii","hello","heyy",1,4,1}
print(type(my_set))
print(my_set)
#print(my_set[2]) we cannot perform this because it has no order(also we cannot add a set inside a set like other)


#dictionary{} has a key:value pair,ordered
my_dict={"name":"man","age":0,"place":"earth",11:11}
print(type(my_dict))
print(my_dict)
my_dict["name"]="human"#by this we can assign a new value to the key
print(my_dict)
#print(my_dict[3])  we cannot access with index numbers
print(my_dict["place"],my_dict["name"])#this way we can get the value assigned to the key
my_dict1={"name":"man","age":0,"list":["w","o","w"],"set":{"w","o","w"},11:11}
print(my_dict1["list"],my_dict1["set"])#we can add set and list inside a dict but only as a value not as an key
print(my_dict1["list"][0])

#boolean



