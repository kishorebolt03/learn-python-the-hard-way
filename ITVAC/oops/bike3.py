class Showroom:
    def __init__(self,ALL):

        self.set_data(*ALL.split(","))

    def set_data(self,ID,name,email,brand,city):
        self.__ID=ID
        self.__name=name
        self.__email=email
        self.__brand=brand
        self.__city=city

    def get_data(self):
        print("ID:",self.__ID)
        print("NAME:",self.__name)
        print("email:",self.__email)
        print("brand :",self.__brand)
        print("city :",self.__city)

    def map(allObj):
        d={}
        for i in allObj:
            d[i.__city]=[i.__city for i in allObj].count(i.__city)
        print("City    Count")
        for i,j in d.items():
            print("{:20}{}".format(i,j))



allObj=[]
for j in range(int(input())):
    allObj.append(Showroom(input()))
    allObj[j].get_data()
Showroom.map(allObj)
'''
#8741BLR,Jack Suzuki,jacksonsuzuki@yahoo.com,Suzuki,Bangalore
#4785BLR,Balaji Bajaj,balaji.bajaj@yahhoo.com,Bajaj,Bangalore
#5478HSRA,Sai Ram Bajaj,srirambajaj@gmail.com,Bajaj,Hosur
#4123CHN,Kick start Suzuki,kickstartsuzuki@gmail.com,Suzuki,Chennai
#6541CHN,Benjamin Honda,benjaminhonda@gmail.com,Honda,Chennai
'''
