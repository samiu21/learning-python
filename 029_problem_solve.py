# simple problem solving using string
# input : x3b4U5i2
# output : bbbbiiUUUUUii

a = input("Enter the input ")
res = " "
for i in range(0, len(a), 2):
    res = res + a[i]*int(a[i+1])
result = sorted(res, key=str.casefold)
re = "".join(result)
print(re)

# palindrome string checking
a = input("Enter the string  ")
if a == a[::-1]:
    print("Yes, this string is palindrome ")
else:
    print("This is string is not palindrome ")

# string reversing
# input: "i Love coding using PYthon"
# output:"i evol gnidoc gnisu nohtyp"

d = input("")
d = d.split(" ")
ress = ""
for i in d:
    ress = ress+i[::-1] + " "
print(ress)
