area = lambda length,width:length*width
perimeter = lambda length, width: 2 * (length + width)


length = int(input("Enter length: "))
width = int(input("Enter width: "))

print("Area : ",area(length,width))
print("Perimeter : ",perimeter(length,width))
