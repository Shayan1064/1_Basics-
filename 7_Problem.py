# Simple Salary Slip Generator

name = input("Enter Employee Name: ")
basic = float(input("Enter Basic Salary: "))

# Calculations
hra = 0.20 * basic
da = 0.10 * basic
ta = 0.05 * basic
pf = 0.12 * basic

gross = basic + hra + da + ta
net = gross - pf

# Output
print("\n--- Salary Slip ---")
print("Employee Name:", name)
print("Basic Salary :", basic)
print("Gross Salary :", gross)
print("Net Salary   :", net)
