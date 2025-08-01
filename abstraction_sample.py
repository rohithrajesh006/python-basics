from abc import ABC,abstractmethod

from list_sample import zaman_list


class parent(ABC):
    @abstractmethod
    def fun(self):
        pass
class child(parent):
    def display(self):
        print("hii")
    def fun(self):
        print("Abstraction method implementation")

ob=child()
ob.display()
ob.fun()
