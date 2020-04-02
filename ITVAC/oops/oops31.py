class Student:
    global re
    def __init__(self,stu):
        self.stu=stu
        self.total=sum(self.stu[2:])
        self.avg=self.total//5
        self.stu.append(self.total)
        if self.total <200:
            re.append(stu)
        self.stu.append(self.avg)
        #print(self.stu)
        #print(self.total,self.avg)

    def sec_topper(stu):
        stu1=sorted(stu,key=lambda x:x.total,reverse=True)
        print(stu1[0].stu)
        print()


    def overall_topper(stu):
        stu1=sorted(stu,key=lambda x:x.total,reverse=True)
        for i in range(5):print(stu1[i].stu)

    def retest():
        print(re)


if __name__=='__main__':
    allClass=[]
    re=[]
    for i in range(3):
        sec=[]
        n=int(input())
        for i in range(n):
            #roll,name,maths,sci,eng,soc,lang
            sec.append(Student([int(input()),input(),int(input()),int(input()),int(input()),int(input()),int(input())]))
        allClass.append(sec)
    for i in allClass:
        #print(i)
        Student.sec_topper(i)
    allClass1=[k for i in allClass for k in i]
    Student.overall_topper(allClass1)
    print("retest")
    Student.retest()

'''
INPUT
2
1
ram
100
100
100
100
99
2
sita
78
45
56
56
78
2
3
rahul
100
99
99
99
99
4
ravi
23
45
45
56
45
2
5
riya
67
5
12
12
23
6
pavi
99
98
98
97
98
'''
