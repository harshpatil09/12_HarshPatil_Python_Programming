s1={1,2,3}
s2={2,3,4}
print(s1,s2)

print("Interaction in s1 and s2: ",s1.intersection(s2))

print("Union: ",s1.union(s2))

print("Non comman elements: ",s1.symmetric_difference(s2))

s1.update(s2)
print("Update set: ",s1)

l1=[1,2,3,4]
s1=set(s1)
print(l1,s1)