while True:
    try:
        number = int(input("Please enter an integer: "))
        print(f"Valid integer received: {number}")
        break
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")