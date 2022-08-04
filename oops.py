# class MyClass:
#     x = 5
# p1 = MyClass()
# print(p1.x)

class Person:
    def __init__(object, name,age):
        object.name = name
        object.age = age
    def myfunc(abc):
        print("Hello my name is "+ abc.name + " and my age is"  +str(abc.age))
p1 = Person('John',35)
p1.myfunc()