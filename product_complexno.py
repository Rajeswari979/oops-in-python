class productOfComplex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
        
    def display(self):
        print(f'{self.real} + {self.imag}i')

    def multiplication(self,dup):
        self.real=(self.real*dup.real)-(self.imag*dup.imag)
        self.imag=(self.real*dup.imag)+(self.imag*dup.real)
 
obj1=productOfComplex(2,2)
obj2=productOfComplex(2,2)
obj1.multiplication(obj2)
obj1.display()  
 
