my_list=[11,22,33,44,55,66]

for list in my_list:
    print(list,end="|")

print("")

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

"""for dict in my_dict:
    print(dict,end=":")
    print(my_dict[dict])
print(my_dict.items())
for dict in my_dict.items():
    print(dict)
"""
for a,b in my_dict.items():
    print(a,b)
