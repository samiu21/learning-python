# problem 1:
# Take two values of length and breadth from the user and check if it is a square or not.
length=float(input("Enter the length :"))
breadth=float(input("Enter the breadth :"))

if length == breadth:
    print("It is a square")
else:
    print("it is not a square")
    
#problem 2:
#Take three input from the user and find the largest number between using if-elif=else statement.
num1 = float (input("Enter first number:"))
num2 = float (input("Enter second number:"))
num3 = float (input("Enter third number:"))

if num1 == num2 and num2==num3:
    print("All numbers are equal")
    

elif num1>=num2 and num1>=num3:
    print("The largest number is :",num1)
    
elif num2>=num1 and num2>=num3:
    print("The largest number is :",num2)
else:
    print("The largest number is :",num3)

#problem 3:
#find the number even or odd
number1 = int (input("Enter a number:"))
if number1%2==0:
    print(number1," is even number")
else:
    print(number1," is odd number")

#problem 4:
# taking the number and find the grade 
marks=float(input("Enter your marks:"))
if marks >90:
    print("Grade A")
elif marks >80 and marks <=90:
    print("Grade B")
elif marks >60 and marks <=80:
    print("Grade C")
elif marks <60 and marks >=33:
    print("Grade D")
    
else:
    print("You are failed")

#problem 5:
#to check whether a year is leap year or not
year = int (input("Enter a year:"))
if year%400==0 and year%100==0:
    print(year, "is a leap year")
elif year%4==0 and year%100!=0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")