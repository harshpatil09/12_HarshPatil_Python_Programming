import array as arr 
a=arr.array('i',[1,2,3])
print("New Array: ")
for i in range(0,3):
    print(a[i],end=' ')
print("\n")

a1=arr.array('d',[2.5,1.5,3.5])
print("Float array : ")
for i in range(0,3):
    print(a1[i],end=' ')
print("\n")

a.insert(1,4)
print("a.insert(1,4) :",a)
print("\n")


a.append(5)
print("a.append(5) :")
for i in range(0,5):
    print(a[i],end=' ')
print("\n")


a.remove(2)
a.pop()
print("a.remove(2) & a.pop(): ")
for i in range(0,3):
    print(a[i],end=' ')
print("\n")



