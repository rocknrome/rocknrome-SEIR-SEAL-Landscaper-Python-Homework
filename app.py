import os

# Global variables declaration
tools = [
    "Teeth",
    "Rusty Scissors",
    "Old-Timey Push Lawnmower",
    "Fancy Battery-Powered Lawnmower",
    "Team of Starving Students"
]

bank_account = 0
earnings = 0
current_tool = tools[0]

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Implementing work day logic
while True:
    clear_console()
    print(f"\nCurrent Tool: {current_tool}")
    print(f"Bank Account: ${bank_account}")

    # Checking the win condition
    if bank_account >= 1000 and current_tool == tools[-1]:
        print("****************************************")
        print("** Congratulations! You won the game! **")
        print("****************************************")
        break

    # Offering choices
    print("\nWhat do you want to do today?")
    print(" 0: Work today")
    print(" 1: Do not work today")
    print(" 2: Upgrade tool")

    choice = int(input("Enter your choice: "))

    # Switch-case for choice logic
    if choice == 0:
        print("* You chose to work today *")
        # Updating bank account based on the tool used
        if current_tool == tools[0]:
            bank_account += 1
        elif current_tool == tools[1]:
            bank_account += 5
        elif current_tool == tools[2]:
            bank_account += 50
        elif current_tool == tools[3]:
            bank_account += 100
        elif current_tool == tools[4]:
            bank_account += 250
    elif choice == 1:
        clear_console()
        print("* You chose not to work today *")
        print("----------------------------------")
    elif choice == 2:
        print("* You chose to upgrade your tool *")
        # Implementing upgrade tool logic
        if current_tool == tools[0] and bank_account >= 5:
            current_tool = tools[1]
            bank_account -= 5
        elif current_tool == tools[1] and bank_account >= 25:
            current_tool = tools[2]
            bank_account -= 25
        elif current_tool == tools[2] and bank_account >= 250:
            current_tool = tools[3]
            bank_account -= 250
        elif current_tool == tools[3] and bank_account >= 500:
            current_tool = tools[4]
            bank_account -= 500
        else:
            print("** But you don't have enough money to upgrade **")
    else:
        clear_console()
        print("Invalid choice. Please choose 0, 1, or 2.")

# End of the game
