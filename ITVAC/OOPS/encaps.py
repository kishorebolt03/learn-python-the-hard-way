class Variables:
    _age=34
    def __init__(self):
        self.name="python"
        self._rollno=1
        self.__age=34
    def printage(self):
        
        print("age is only accessed only inside class age=",self.__age)


if __name__=="__main__":
    obj=Variables()
    print(obj.name)
    print(obj._rollno)
    print(obj._Variables__age)

