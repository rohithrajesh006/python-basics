from logging import exception

a=10
b=0
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("zero division error")
except NameError:
    print("value not defined")
except Exception as e:
    print("error",e)
print("finished")







try:
    my_list=[1,2,3]
    print(my_list[5])
except Exception as e:
    print(e)



