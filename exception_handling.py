while True:
    try:
        number = int(input("Please enter an integer: "))
        print(f"Valid integer received: {number}")
        break
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

#raise error
def square(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return x * x