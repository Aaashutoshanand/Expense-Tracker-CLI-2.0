import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

# Initialize file
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Description", "Amount", "Category", "Date"])

# Add expense
def add_expense():
    desc = input("Enter description: ")

    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("❌ Enter a valid number!")

    category = input("Enter category: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount, category, date])

    print("✅ Expense added!")

# View expenses
def view_expenses():
    print("\n📋 All Expenses:\n")

    try:
        with open(FILE_NAME, "r") as f:
            reader = csv.reader(f)
            next(reader, None)

            for i, row in enumerate(reader, start=1):
                print(f"{i}. {row[0]} | ₹{row[1]} | {row[2]} | {row[3]}")

    except FileNotFoundError:
        print("No data found.")

# Search by category
def search_by_category():
    category = input("Enter category: ")

    print(f"\n🔍 Results for '{category}':\n")

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader, None)

        found = False
        for row in reader:
            if row[2].lower() == category.lower():
                print(f"{row[0]} | ₹{row[1]} | {row[3]}")
                found = True

        if not found:
            print("No matching expenses.")

# Total per category
def total_by_category():
    totals = {}

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            cat = row[2]
            amt = float(row[1])
            totals[cat] = totals.get(cat, 0) + amt

    print("\n📊 Total per Category:")
    for cat, total in totals.items():
        print(f"{cat}: ₹{total}")

# Monthly spending
def monthly_spending():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            if row[3].startswith(month):
                total += float(row[1])

    print(f"\n📅 Total for {month}: ₹{total}")

# Top category
def top_category():
    totals = {}

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            cat = row[2]
            amt = float(row[1])
            totals[cat] = totals.get(cat, 0) + amt

    if totals:
        top = max(totals, key=totals.get)
        print(f"\n🔥 Top category: {top} → ₹{totals[top]}")
    else:
        print("No data available.")

# Delete expense
def delete_expense():
    rows = []

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if len(rows) <= 1:
        print("No expenses to delete.")
        return

    print("\nSelect expense to delete:\n")
    for i, row in enumerate(rows[1:], start=1):
        print(f"{i}. {row[0]} | ₹{row[1]} | {row[2]} | {row[3]}")

    try:
        choice = int(input("Enter number: "))
        if 1 <= choice < len(rows):
            rows.pop(choice)
        else:
            print("Invalid choice.")
            return
    except:
        print("Invalid input.")
        return

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print("🗑️ Expense deleted!")

# Summary
def summary():
    total = 0
    count = 0

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            total += float(row[1])
            count += 1

    avg = total / count if count else 0

    print("\n📊 Summary:")
    print(f"Total Expenses: ₹{total}")
    print(f"Number of Entries: {count}")
    print(f"Average Expense: ₹{avg:.2f}")

# Menu
def menu():
    initialize_file()

    while True:
        print("\n====== 💰 Expense Tracker 2.0 ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. Total per Category")
        print("5. Monthly Spending")
        print("6. Top Category")
        print("7. Delete Expense")
        print("8. Summary")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_by_category()
        elif choice == "4":
            total_by_category()
        elif choice == "5":
            monthly_spending()
        elif choice == "6":
            top_category()
        elif choice == "7":
            delete_expense()
        elif choice == "8":
            summary()
        elif choice == "9":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

# Run program
menu()