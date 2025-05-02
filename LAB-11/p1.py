while True:
    try:
        num = int(input("Enter an integer: "))
        print(f"You entered: {num}")
        break
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid integer.")
