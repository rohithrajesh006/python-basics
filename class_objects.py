"""class laptops:
    def spec(self):
        self.ram="8gb"
        self.model="hp"
lap1=laptops()
lap1.spec()
print(lap1.ram,lap1.model)"""

class laptops:
    owner="rohith"
    def __init__(self,a,b):
        self.ram = a
        self.model = b

    def spec(self,r,m):
        pass
lap1=laptops("16 gb","acer")
lap2=laptops("16 gb","hp")
print(lap1.ram,lap1.model)
print(lap2.ram)
print(laptops.owner)
