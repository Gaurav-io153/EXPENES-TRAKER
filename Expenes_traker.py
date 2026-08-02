listed = []
print("WELCOME TO THE EXPENSE TRACKER")
print(30 * '=')

while True:
    asking = input("Enter option (add, view, total, exit): ").strip().lower()

    if asking == 'add':
        add_ = input("Enter expense TYPE: ")
        
        # Safe input handling for numbers
        try:
            amount = int(input("Enter money of expense: "))
        except ValueError:
            print("Please enter a valid number for the amount!")
            print(30 * '=')
            continue

        tracker = {
            'type': add_,
            'EXPENSE_MONEY': amount
        }
        listed.append(tracker)

        # Corrected file mode and newline formatting
        with open("View_expenses.txt", "a") as file:
            file.write(f"{add_} : ${amount}\n")

        print("EXPENSE ADDED SUCCESSFULLY")
        print(30 * '=')

    elif asking == 'view':
        # Handles case where the file hasn't been created yet
        try:
            with open("View_expenses.txt", "r") as file:
                content = file.read()
                if content:
                    print(content.strip())
                else:
                    print("No expenses recorded yet.")
        except FileNotFoundError:
            print("No expenses file found yet. Add an expense first!")

        print(30 * '=')

    elif asking == 'total':
        total = sum(item['EXPENSE_MONEY'] for item in listed)
        print(f'TOTAL EXPENSE AMOUNT: ${total}')
        print(f"ALL EXPENSE RECORDS: {listed}")
        print(30 * '=')

    elif asking == 'exit':
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose add, view, total, or exit.")
        print(30 * '=')