# lower() : converts character into lowercase
a = "Hello WoRLD PYthOn"
print(a.lower())
print(a)
# upper() : converts character into uppercase
print(a.upper())

# tittle() : converts string to title case
print(a.title())

print("Hello".isupper())
print("hello".islower())
print("HellO".istitle())
x = "hello"
print(x.isalpha())
# title() : Every letter of a world will be capital
# capitalize() : only first letter will be capital
print(a.capitalize())
# swapcase : capital letter will be small and small letter will be capital
print(a.swapcase())
# casefold() : casefold () is more powerful than .lower() function
# text = groß  it will be gross if we use casefold() but if we use .lower() it will not change and it will be same
print(a.casefold())
# replace() : change the word
xyz = "Hello world"
xyz2 = xyz.replace('e', 'x', 1)
print(xyz2)
# count() : it will print how much time a letter in the word or sentence
print(xyz.count('l'))
# .isdigit() it shows if any digit in the sentence
print(xyz.isdigit())

# joint() >>> list to string convert
# split() , list() --> string to list convert
d = ["h", "e", "l", "l", "o"]
print("".join(d))
e = ["1", "2", "3"]
print("".join(e))

h = "hello world hello world"
v = h.split()
print(v)
c = list(h)
print(c)
