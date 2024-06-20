class Student:
    # def __init__(self,r_no,name,mark):
    #     self.r_no=r_no
    #     self.name=name
    #     self.mark=mark
    r_no=0
    name=''
    mark=[]
    def display(self):
        print(f'{self.r_no}')
        print(f'{self.name}')
        print(f'{self.mark}')

obj1=Student()
obj1.r_no=12
obj1.name="raji"
obj1.mark=[100,98,76]
obj1.display()
