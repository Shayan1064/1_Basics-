# Take input of 5 subjects’ marks and calculate the total, average, and percentage.

# Marks of 5 subjects (you can also take input from user)
m1 = 98
m2 = 95
m3 = 93
m4 = 91
m5 = 97

# Total marks obtained
total = m1 + m2 + m3 + m4 + m5

# Average
average = total / 5

# Assuming each subject is out of 100 → total marks = 500
percentage = (total / 500) * 100

# Output
print("Total Marks:", total)
print("Average Marks:", average)
print("Percentage:", percentage, "%")
