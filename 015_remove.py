fruits = ["apple", "Banana", "orange", "Jackfruit", "pineapple"]
fruits.remove("Banana")   # it will remove only specific item
print(fruits)

animal = ["cow", "goat", "HEn", "Duck", "Cat", "Dog", "Horse", "Ass"]
animal.pop(2)    # it will also remove specific item
print(animal)

animal.pop()    # we do not use any index last item will remove
print(animal)

fruits2 = ["apple", "Banana", "orange", "Jackfruit", "pineapple"]
del fruits2[3]    # specifi item will remove
print(fruits2)

del fruits2    # it will delete the full list with variable

animal2 = ["cow", "goat", "HEn", "Duck", "Cat", "Dog", "Horse", "Ass"]
animal2.clear()   # it will delete the item but not the variable
print(animal2)

animal2 = ["Dolphin", "Hilsa", "Rupchanda"]
print(animal2)     # using clear the list again we can use that variable
