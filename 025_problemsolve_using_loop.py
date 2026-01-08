# problem 1
# Multiplication table
a = int(input("Enter a number :  "))
for i in range(1, 11):
    print(a, " * ", i, " = ", a*i)

# problem 2
# Factorial of a number
n = int(input("Enter a number : "))
factorial = 1
for i in range(1, n+1):
    factorial = factorial * i
print("Factorial of ", n, " is ", factorial)

# problem 3
# Fibonacci series 0 1 1 2 3 5 8 13
number = int(input("Enter the number of terms in the Fibonacci series: "))
a, b = 1, 2
for i in range(number):
    print(a, end=" ")
    result = a + b
    a = b
    b = result

# problem 4
# Digit count of a number
# longest method
number1 = int(input("Enter a number: "))
count = 0
while number1 > 0:
    number1 //= 10
    count += 1
print("Digit count of the number is: ", count)

# shortest method
number2 = input("Enter a number : ")
print("Digit count of the number is : ", len(number2))
