# Write a program that calculates the area and perimeter 
# of a rectangle from user input.


def area(length,width):
    a=length*width
    print("The area of rectangle is : ",a)

def perimeter(length,width):
    p=2*(length+width)
    print("The Perimeter of rectangle is : ",p)


Length=int(input("Enter Your Length : "))
width=int(input("Enter Your Width : "))

area(Length,width)
perimeter(Length,width)