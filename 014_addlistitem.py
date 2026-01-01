# #adding item using append function
# fruit=["Mango","Banana","Jackfruit","Palm","Black plum","Lychee"]
# fruit.append("Olive")   #append use last index to add only one item
# print(fruit)

# extend function use more item to add in the last index
# fruit.extend(["Tamarind","Pear"])
# print(fruit)

# adding item using insert function at any index  item can be duplicate if we use more time
animal = ["cow", "goat", "hen", "duck"]
print(animal)
animal.insert(2, "Bear")  # add only one item at a time
print(animal)

# multiple item add to need slice function
animal[2:2] = ["cat", "dog", "Tiger",  "Lion"]  # 4 item will be add in  index 2 and no item will be removed
print(animal)

animal[2:3] = ["cat", "dog", "Tiger", "Lion"]  # index number 2 item will be delete and 4 item will be add in index 2
print(animal)

animal[2:4] = ["cat", "dog", "Tiger", "Lion"]  # index number 2 and 3 will be delete and 4 item will be add
print(animal)
