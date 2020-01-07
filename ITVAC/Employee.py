import sys

class Employee:
    def __init__(s):
        s.emp_name=''
        s.emp_salary=0
        s.emp_ID=''
        s.emp_dsgn=''
        s.emp_level=''
        s.Input_data()            
    
    def Input_data(s):
        s.emp_name=input("enter name ")
        s.emp_ID=input("enter ID ")
        s.emp_dsgn=input("enter designation ")
        s.emp_salary=int(input("enter salary"))
    def allocate_levels(s):
        if s.emp_salary>=25000:
            s.emp_level='A'
        elif s.emp_salary>=20000 and s.emp_salary<25000:
            s.emp_level='B'
        elif s.emp_salary>=15000 and s.emp_salary<20000:
            s.emp_level='C'
        else:
            s.emp_level='D'
    def show(s):
        for k,v in s.__dict__.items():
            print(k,":",v,"size=",sys.getsizeof(k))

        
def get_data(obj):
    for i in range(len(obj)):
        print("enter the employee {} details".format(i+1))
        obj[i]=Employee()
        print("size-----------------------------",sys.getsizeof(obj[i].emp_name))
def get_max_sal(obj):
    maxx=0
    for i in range(len(obj)):
        obj[i].allocate_levels()
        obj[i].show()
        print(end='')
        if obj[i].emp_salary>maxx:
            maxx=obj[i].emp_salary
            indx=i
    print()
    print("maximum salary is got by ",end='')
    print(obj[indx].emp_name)


def main():
    obj=[i for i in range(int(input("enter num of employees")))]
    get_data(obj)
    
    get_max_sal(obj)
if __name__=='__main__':
    main()
