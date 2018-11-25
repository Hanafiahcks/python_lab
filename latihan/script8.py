file =open('latihan.txt','w')
dir(file)
file.write('line 1\n')
file.write('line 2\n')
list=["Line 3","Line 4","Line 5"]
for l in list:
    file.write(l+"\n")
file.close()
