# 8.Write a menu-driven program to implement the Queue data structure.

# Define the queue
queue = []

# Function to display the menu
def display_menu():
    print("\nQueue Operations Menu:")
    print("1. Enqueue (Add an element to the queue)")
    print("2. Dequeue (Remove an element from the queue)")
    print("3. Display the queue")
    print("4. Exit")

# Main program
while True:
    display_menu()
    
    # Accept the user's choice
    choice = input("Enter your choice (1-4): ")
    
    # Perform the corresponding operation
    if choice == '1':
        element = input("Enter the element to add to the queue: ")
        queue.append(element)
        print(f"Element '{element}' added to the queue.")
    
    elif choice == '2':
        if queue:
            dequeued_element = queue.pop(0)
            print(f"Element '{dequeued_element}' removed from the queue.")
        else:
            print("The queue is empty. No element to remove.")
    
    elif choice == '3':
        if queue:
            print("Current queue:", queue)
        else:
            print("The queue is empty.")
    
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
