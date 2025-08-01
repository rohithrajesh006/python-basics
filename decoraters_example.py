def swap(fun):
    def wrapper(A,B):
        if A<B:
            A,B=B,A
            fun(A,B)
    return wrapper

@swap
def subtract(a,b):
    c=a-b
    print(c)
subtract(5,10)