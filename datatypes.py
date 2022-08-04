#list
'''first = ['shivam','rinki','shirinki']
# print(first[2])
first.insert(1,'jaiswal')

first.append('dictionary')

tropical = ('mango','pineapple','cherry','aple')
first.extend(tropical)
first.pop(4)

first.sort(reverse = True)
print(first)


#tuple
mytuple = ("banana","apple","mango")
y = list(mytuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#set are unorganized
set = {'apple','banana','cherry'}
set.add("orange")
set.remove("banana")
print(set)

#dictionary
car = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1996
}

x = car.items()
car['color'] = "black"
print(x)
print(car.keys())'''
a = tuple(("rinki","jaiswal", "shivam", "jaiswal"))
print(type(a))