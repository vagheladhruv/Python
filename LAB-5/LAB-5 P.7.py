#7.Write a menu-driven program to implement the stack data structure.

# Define the stack
stack = []

# Function to display the menu
def display_menu():
    print("\nStack Operations Menu:")
    print("1. Push an element onto the stack")
    print("2. Pop an element from the stack")
    print("3. Display the stack")
    print("4. Exit")

# Main program
while True:
    display_menu()
    
    # Accept the user's choice
    choice = input("Enter your choice (1-4): ")
    
    # Perform the corresponding operation
    if choice == '1':
        element = input("Enter the element to push onto the stack: ")
        stack.append(element)
        print(f"Element '{element}' pushed onto the stack.")
    
    elif choice == '2':
        if stack:
            popped_element = stack.pop()
            print(f"Element '{popped_element}' popped from the stack.")
        else:
            print("The stack is empty. No element to pop.")
    
    elif choice == '3':
        if stack:
            print("Current stack:", stack)
        else:
            print("The stack is empty.")
    
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
