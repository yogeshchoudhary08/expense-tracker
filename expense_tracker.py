import json

def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def add_expense(expenses):
    date = input("Enter date (DD-MM-YYYY): ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ").capitalize()
    
    expenses.append({
        "date": date,
        "amount": amount,
        "category": category
    })
    
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=2)
    print("Expense added successfully!")

def main():
    expenses = load_expenses()
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add New Expense")
        print("2. Exit")
        choice = input("Choose option (1-2): ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()