class MetaClassWithPrint(type):
    def __new__(cls, clsname, bases, clsdict):
        print(f"Створено новий клас: {clsname}")
        return super().__new__(cls, clsname, bases, clsdict)


class MyClass(metaclass=MetaClassWithPrint):
    def __init__(self):
        pass


class AnotherClass(MyClass):
    pass
