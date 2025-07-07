# print pattern
#
# #
# # #
# # # #


row=input("Enter the number of rows: ")
column=input("Enter the number of columns: ")

for i in range(int(row)):
    for j in range(int(column)):
        if j<=i:
            print("#", end=" ")
    print()
    
# another way to print the same pattern
for i in range(7):
    for j in range(i):
        print("#",end = " ")
    print()
 
 # another pattern
#   a
#   a b 
#   a b c 
#   a b c d

for i in range(4):
    for j in range(i+1):
        print(chr(97+j), end=" ")
    print()