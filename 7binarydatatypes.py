list1 =[1,2,3,4,3,6,9,255]  #immutable, range(0-255)
b=bytes(list1)
print(b)
print(type(b))

list2 =[1,2,3,4,3,6,9,255]  #mutable, range (0 -255)
b1=bytearray(list1) 
print(b1)
print(type(b1))