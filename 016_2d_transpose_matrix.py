# for loop use kore 2D matrix comprehension

matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
a = []
for row in range(2):
    b = []
    for col in matrix:
        b.append(col[row])
    a.append(b)
print(a)


# list comprehension use kore

res = [[col[row] for col in matrix] for row in range(2)]
print(res)
