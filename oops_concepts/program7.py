class Fruit:
    __hiddenFruit="Guava"
    __hiddenFruitnumber=3
    def __init__(self):
        pass
    def __repr__(self):
        return "Fruit details :%s:"%self.__hiddenFruit
    def add(self,increment):
        #print(self.__hiddenFruitnumber)
        self.__hiddenFruitnumber=self.__hiddenFruitnumber+increment
        print("There are {}  {} in the basket".format(self.__hiddenFruitnumber,self.__hiddenFruit))

basket=Fruit()
print(Fruit())