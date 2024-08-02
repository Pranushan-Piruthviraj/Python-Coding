a = {}
a["fruits"] = ["apple", "banana"]
a["vegetables"] = ['potato', "onion"]
print(a)
print(len(a))
a["fruits"] = ["kiwi"]
print(a)
print(type(a["fruits"]))
a["fruits"].append("pineapple")
a["fruits_new"] = ["kiwi", "pineapple"]
print(a)
del a["fruits_new"]
print(a)
print(a.get("juices"))
print(a.get("fruits"))
a["juices"] = ["Cramberry", "orange"]
for element in a:
    print(element)
    print(a[element])
for key,value in a.items():
    print(key)
    print(value)
for value in a.values():
    print(value)
for key in a.keys():
    print(key)
a[0] = 2
a[1] = 3
print(a)
print(a.items())
print(a.values())
print(a.keys())
# a[["fruits","vegetables"]] = ["cherry","carrot"]
# print(a)
b = {"fruits":["watermelon","grapes"], "vegetables":["lettuce","beets"]}
comb = [a,b]
print(comb)
name = input("Please enter your name: ")
print("hey you entered name: " + name)
age = input("Enter your age: ")
print(type(age))
print("your age: " + str(age))
fruits = input("Please add list of fruits to buy: ")
print(list(fruits))