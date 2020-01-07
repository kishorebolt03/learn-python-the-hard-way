class Student:
    def __init__(s,name,roll):
        print("instanciating Objects")
        s.name=name
        s.roll=roll
        s.display()
    def display(s):
        print("name ----------",s.name)
        print("ROllnumber-------",s.roll)
    def __del__(s):
        print("Deleting the Objects")



obj=Student('rughal',12)
print(obj.name)
del obj
print(obj.name)
