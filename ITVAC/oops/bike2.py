import re

class Bike:
    __VIN=''
    __brand=''
    __model=''
    __engDisp=''
    __brakeSys=''
    __cost=0.0
    def __init__(self,__VIN, __brand, __model,__engDisp,__brakeSys,__cost):
        self.__VIN=__VIN
        self.__brand=__brand
        self.__model=__model
        self.__engDisp=__engDisp
        self.__brakeSys=__brakeSys
        self.__cost=__cost


    def display(self):
        print("VIN:",self.__VIN)
        print("brand:",self.__brand)
        print("model:",self.__model)
        print("endineDisplacement :",self.__engDisp)
        print("brake System :",self.__brakeSys)
        print("cost :",self.__cost)
        self.validateVIN()


    def validateVIN(self):
        flg=0
        match = re.match(r'^[A-Z0-9]{3}[A-Z]{2}[0-9]{1}[A-Z0-9]{1}[0-9]{2}[A-Z0-9]{2}[0-9]{6}$',str(self.__VIN))
        print()
        print(self.__VIN)
        print("VIN is valid") if match else print('VIN is not valid')



Bike1=Bike(*input().split(","))
#Bike2=Bike(*input().split(","))
Bike1.display()
#Bike2.display()



'''
MD2GJ3214JR258416,KTM,RC,390cc,Disk,225000.0
MD2GJ3214JR258416,KTM,RC,390cc,Disk,225000.0
ME1CF23844HN874621,BMW,S,1000cc,Disk,1800000.0
'''
