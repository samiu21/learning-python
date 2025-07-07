#problem 1
#armstrong number check

a = int(input("Enter a number "))
leng=(len(str(a)))
temp=a
sum=0
while temp>0:
    b=temp%10
    sum=sum+b**leng
    temp=temp//10
    
if a==sum:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")

# finding armstrong number in another way
b=int (input("Enter a number "))
sum=0
n=str(b)
length=len(n)
for i in n:
    sum = sum+int (i)**length
    
if b==sum:
    print("This number is an Armstrong number ")
else:
    print("This number is not an Armstrong number ")
    
# problem 2
#reverse a number
number3=int (input("Enter a number to reverse: "))
reveresee=0
while number3>0:
    digit=number3%10
    reveresee=reveresee*10+digit
    number3=number3//10
    
print("The reverse of the number is : ", reveresee)