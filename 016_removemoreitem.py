fruits=["apple","Banana","orange","Jackfruit","pineapple"]
del fruits[1:4]   #index 1 to 3 will remove
print(fruits)

fruits = ["apple", "banana", "orange", "jackfruit", "pineapple"]
to_remove = ["banana", "jackfruit"]

for item in to_remove:
    if item in fruits:
        fruits.remove(item) 
            

print(fruits)
# Output: ['apple', 'orange', 'pineapple']
