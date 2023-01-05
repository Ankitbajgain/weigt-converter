weight = input("Enter your weight: ")
unit = input("kg or lbs: ")
if unit == "kg":
    converted = int(weight) / 0.45
    print(f"You are {converted} pounds")

elif unit == "lbs":
    converted = int(weight) * 0.45
    print(f"You are {converted} kilograms")
