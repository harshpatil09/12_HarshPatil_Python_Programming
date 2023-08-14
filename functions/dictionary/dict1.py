d1={1:"hello",2:"hi",'a':"Welcome"}
print("d1 : ",d1)
print()
print("Print keys : ",d1.keys())

print("Print Items & keys : ",d1.items())

print("To get value of a : ",d1.get('a'))
print()

newd=d1.copy()
print("Copy d1 : ",newd);print()

print("Pop value at index 1 : ",d1.pop(1))
print("d1 :",d1);print()

print("Pop all items in dictionary : ",d1.popitem())
print("d1 : ",d1);print()

d2={4:"welcome"}
print("d2 : ",d2)
d1.update(d2)
print("Updated d1 is : ",d1);print()

d1.clear()
print("d1.clear() : ",d1);print()

d3={'a','b','c'}
print("d3 : ",d3);print()

d4=dict.fromkeys(d3,1)
print("Adding key to d3 values : ",d4);print()

#d1.update(5:"hello",'g':"DYP")
print("d1.update(5:'hello','g':'DYP')")
print("Update d1 : ",d1)