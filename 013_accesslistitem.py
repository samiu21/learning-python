fruit = ["Mango", "Banana", "Jackfruit", "Palm", "Black plum", "Lychee"]
print(fruit)
print(fruit[3])             # access the item of the list
fruit[2] = "Almond"
print(fruit)        # fruit[2]=jackfruit will replace by Almond


print(fruit[-1])   # output = Lychee
print(fruit[-2])   # output = Black plum
print(fruit[-4])   # output = Jackfruit not it will Almond becacuse we replace this index value with Almond
