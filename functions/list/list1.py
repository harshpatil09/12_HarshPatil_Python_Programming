l1=[1,2,"hello",3.4]
print(l1,"\n")
print("Type : ",type(l1))
print()

print("l1[2:] : ",l1[2:])

print("l1[:] : ",l1[:])

print("l1[1:4:2] : ",l1[0:4:2])

print("l1[-3:-1] : ",l1[-3:-1])

l1[2]=10
print(l1)

l1[2:4]=[84,36]
print(l1)

#repetation
print("\nRepetation")
l2=l1*2
print(l2)

#concatenation
print("Concatination")
l3=l1+l2
print(l3)

#iteration
print("Iteration")
for l in l1:
    print(l)

#membership
print("Memebership")
print(1 in l1)


