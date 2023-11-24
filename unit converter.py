def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def length_converter():
    print("Welcome to the Length Converter!")
    print("Choose an option:")
    print("1. Meters to Feet")
    print("2. Feet to Meters")

    choice = input("Enter your choice (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        return

    try:
        value = float(input("Enter the value to convert: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if choice == '1':
        result = meters_to_feet(value)
        print(f"{value} meters is equal to {result:.2f} feet.")
    else:
        result = feet_to_meters(value)
        print(f"{value} feet is equal to {result:.2f} meters.")

length_converter()
def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def length_converter():
    print("Welcome to the Length Converter!")
    print("Choose an option:")
    print("1. Meters to Feet")
    print("2. Feet to Meters")

    choice = input("Enter your choice (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        return

    try:
        value = float(input("Enter the value to convert: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if choice == '1':
        result = meters_to_feet(value)
        print(f"{value} meters is equal to {result:.2f} feet.")
    else:
        result = feet_to_meters(value)
        print(f"{value} feet is equal to {result:.2f} meters.")

length_converter()
def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def length_converter():
    print("Welcome to the Length Converter!")
    print("Choose an option:")
    print("1. Meters to Feet")
    print("2. Feet to Meters")

    choice = input("Enter your choice (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        return

    try:
        value = float(input("Enter the value to convert: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if choice == '1':
        result = meters_to_feet(value)
        print(f"{value} meters is equal to {result:.2f} feet.")
    else:
        result = feet_to_meters(value)
        print(f"{value} feet is equal to {result:.2f} meters.")

length_converter()












