class Num:

    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"value is {self._value}")

    @property
    def ten_value(self):
        return  2*self._value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self._value =  new_value/2
    
a = Num(10)
a.ten_value = 86
print(a.ten_value)
a.show()

    
