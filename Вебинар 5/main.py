x = 20
"""While"""
while True:
    if x > 50:
        break
    if x % 2 == 0:
        print(str(x) + " чётный")
    x += 1
print("всё короче")

while x <= 50:
    x += 1
    if x % 2 != 0:
        continue
    print(str(x) + " чётный")
"""for"""
for c in 'Hello, world!':
    print(c)

for i in range(50):
    print(i)

for i in range(20, 50, 2): # первое число указывает на начало, третье на шаг
    print(i)
"""list"""
names = []

names.append("test")
names.append("test2")
names.append("test3")
names.append("test4")

names[3] = "test4_1"
print(names[3])

while True:
    name = input("Enter new name or end: ")
    if name == "end":
        break
    names.append(name)
    print("all names: ", names)

names = [ "test", "test2", "test3", "test4" ]
print(len(names))

for name in names:
    print(name)

if 'test' in names:
    print('test is here')




