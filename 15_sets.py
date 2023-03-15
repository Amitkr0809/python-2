a = {1,2,3,4,5,6}
print(type(a))
print(a)

b= {} # it create empty 'dict' not 'set'
print(type(b))

# empty set is create ed by
c = set()
print(type (c))

c.add(5) # to add values in set
c.add(4)
print(c)
# c.add([1,2]) # cannot add list in set bcoz set cannot change but list is changeable
# print(c) 

c.add((1,2,3)) # tuple can be added in set
print(c)

print(len(c)) # to print length of set
c.remove(5) # to remove values from set
print(c)
