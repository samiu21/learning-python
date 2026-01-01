# problem 1: Taking multiple string input from user and store them in a list

a = input("Enter multiple string input separated by space for making a list: ") . split()
print("List of items: ", a)

# #problem 2: Taking multiple int input from user and store them in a list
b = list(map(int, input("Enter multiple int input separated by space for making a list: ").split()))
print("List of items: ", b)

# problem 3: Taking multiple float input from user and store them in a list


try:
    c = list(map(float, input("Enter multiple float input separated by space for making a list: ").split()))
    print("List of items: ", c)
except ValueError:
    print("Please enter valid float numbers separated by space.")
