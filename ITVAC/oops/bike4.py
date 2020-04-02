interface comparable:



class Bike:
    def __init__(self,ALL):
        self.set_data(*ALL.split(","))

    def set_data(self,__VIN, __brand, __model,__engDisp,__brakeSys,__cost):
        self.__VIN=__VIN
        self.__brand=__brand
        self.__model=__model
        self.__engDisp=__engDisp
        self.__brakeSys=__brakeSys
        self.__cost=__cost

    def get_data(self):
        print("VIN:",self.__VIN)
        print("brand:",self.__brand)
        print("model:",self.__model)
        print("endineDisplacement :",self.__engDisp)
        print("brake System :",self.__brakeSys)
        print("cost :",self.__cost)

    def createBike(self,String):

Bike1=Bike(input())
Bike2=Bike(input())
Bike1.get_data()
Bike2.get_data()
