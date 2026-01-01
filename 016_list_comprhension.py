# Example: Iteration with list comprehension
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
b = [i+5 for i in a]
print("List comprehension result: ", b)

# example 2 : Iterating through a string using list comprehension
c = "Hello world"
d = [i for i in c]
print("List comprehension result: ", d)
e = list(c)
print("List comprehension result: ", e)

# example 3: using range function in list comprehension
f = [i for i in range(1, 20, 2)]
print("List comprehension result: ", f)
g = list(range(1, 20, 2))
print("List comprehension result: ", g)
# Example 4: Using if with list comprehension
h = [i for i in range(1, 20) if i % 2 == 0]
print("List comprehension result: ", h)

# Example 5: Nested if with list comprehension
k = [i for i in range(1, 20) if i % 3 == 0 or i % 5 == 0]
print("List comprehension result: ", k)

ll = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 20)]
print(ll)
