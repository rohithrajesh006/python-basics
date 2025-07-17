"""for r in range(1,4):
    for j in range(1,r+1):
        #print(j)
        print(j, end=" ")
    print(" ")
"""


"""or p in range(1,5):
    print("*"*p)  """     

"""for a in range(1,6):
    for b in range(5-a):
        print("",end=" ")
    for c in range(a):
        print("* ",end="")
    print("")"""
"""
for a in range(1,6):
    print(" "*int(5-a),"*"*a)

print(list(range(5,0,-1)))"""


"""for a in range(5,0,-1):
    print("* "*a)
"""



"""for a in range(1,5):
    b=a
    for c in range(a):
        print(b,end=" ")
        b=b+a
    print(" ")"""

"""for a in range(1,5):
    for b in range(1,a+1):
        print(a*b,end=" ")
    print(" ")"""

"""for a in range(5,0,-1):
    print(" "*int(5-a),"* "*a)"""


"""for a in range(1,6):
    print(" "*int(5-a),"* "*a)
for b in range(5,0,-1):
    print(" "*int(5-b),"* "*b)
"""

"""for a in range(1,6):
    for b in range(a):
        print(chr(65+b),end=" ")
    print()"""

"""for a in range(1,6):

    k=a
    n=4
    for b in range(1,a+1):
        print(k,end=" ")
        k=k+n
        n-=1
    print()
    """
"""row=4
col=5
for a in range(row):
    for b in range(col):
        if a==0 or a==row-1 or  b==0 or b==col-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()      
"""

