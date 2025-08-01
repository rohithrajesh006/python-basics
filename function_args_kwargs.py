#*args
"""def total(*a):
    print(a)#tuple()
    print(sum(a))

total(1,2,3)"""

#**kwargs
def a(**students):
    print(students)#dict{}
    print(f"my name is {students["name"]} and {students["age"]} years old")

a(name="Athul",age=21)
