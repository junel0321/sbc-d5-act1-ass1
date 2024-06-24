numbers = []

while True:
    command = input("Command: ")

    if command.startswith('add ') and command[4:].isdigit():
        numbers.append(int(command.split()[1]))
        print(f"Added {numbers[-1]} to the list")

    elif command == 'naa':
        print(f"Removed {numbers.pop(0)} from the front (queue)" if numbers else "Queue is empty, cannot remove.")
    elif command == 'wala':
        print(f"Removed {numbers.pop()} from the end (stack)" if numbers else "Stack is empty, cannot remove.")
    elif command == 'display':
        print(f"Current List: {numbers}" if numbers else "List is empty.")
    elif command == 'exit':
        print("Code has been terminated.")
        break
    else:
        print("Invalid command. Please try again.")
