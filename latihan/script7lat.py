file = open('055 fruits.txt','r')
content = file.readlines()
for i in content:
     print(len(i.strip()))
for i in content:
     print(i.strip())
file.close()
