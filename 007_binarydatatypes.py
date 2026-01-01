list1 = [1, 2, 3, 4, 3, 6, 9, 255]  # immutable, range(0-255)
b = bytes(list1)              # both will print  vaule in different forms.
print(b)                    # Here will  print full object How python represents the full bytearray
print(b[3])                 # Here will print specific element
print(type(b))

list2 = [1, 2, 3, 4, 3, 6, 9, 255]  # mutable, range (0 -255)
b1 = bytearray(list2)
list2[3] = 121               # both will print  vaule in different forms.
print(b1)                  # Here will  print full object How python represents the full bytearray
print(b1[1])               # Here will print specific element

print(type(b1))
