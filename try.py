class employee:
    def __init__(self, *args, **kwargs):
        self.name=args[0]
        self.position=args[1]
        print("I am employee")
    pass
    def funcion1(self,*args):
        print(args)
        pass
class employer:
    def __init__(self, *args, **kwargs):
        print("my name is ",args[0])
    pass
xiaowang=employee("小明","管理")
xiaoming=employer("小明")
print(xiaowang.name)
print(xiaowang.position)
xiaowang.funcion1("fs","sf","fs")
class father:
    def speak(self):
        print("I can fly")
        pass
class son(father):
    pass
class mother():
    def power(self):
        print("I have power")
        pass
    pass
class daughter(father,mother):
    def run(self):
        print("I can run")
        pass
    pass
class son2(father):
    def speak(self):
        print("I can fly speed")
d=daughter()
d.power()
d.run()
d.speak()
s2=son2()
s2.speak()