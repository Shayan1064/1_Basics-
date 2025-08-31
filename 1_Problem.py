 # Convert a given number of minutes into hours and minutes
 #  (e.g., 130 minutes → 2 hours 10 minutes).

def converter(minutes):
    hour=minutes//60
    remaining_minutes=minutes%60
    return hour,remaining_minutes


minutes=int(input("Enter Minutes : "))
h,m=converter(minutes)
print(f"Minutes : {minutes} = {h} Hours and {m} Minutes")