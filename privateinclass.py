class person:
    def __init__(self,name):
        self.__pra = name
    def pratik(self, name):
        self.__pra = name

    
p1 = person("hari")
print(p1._person__pra)
p1.pratik('pratik')
print(p1._person__pra)
