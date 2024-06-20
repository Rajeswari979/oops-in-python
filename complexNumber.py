class complexNumber:
    real=0
    imag=0
      
    def display(self):
        print(f'{self.real} + {self.imag}i')

    def subtraction(self,obj2):
        self.real-=obj2.real                 # 3-8
        self.imag=self.imag-obj2.imag        # 5-2

obj1=complexNumber()
obj1.real=3
obj1.imag=5
obj2=complexNumber()
obj2.real=8
obj2.imag=2
obj1.subtraction(obj2)
obj1.display()

