# Write a program to swap two variables without using a third variable.


num1=int(input("Enter Num 1 : "))
num2=int(input("Enter Num 2 : "))

print("Before Swapping")
print(num1," ",num2)
num1,num2=num2,num1

print("After Swapping")
print(num1," ",num2)

