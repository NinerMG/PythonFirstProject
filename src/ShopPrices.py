total_income = 0

def print_prices():
    print('''Prices:
Bubblegum: $2
Toffee: $0.2
Ice cream: $5
Milk chocolate: $4
Doughnut: $2.5
Pancake: $3.2''')

def calculate_earings():
    earings = {
        "Bubblegum" : 202,
        "Toffee" : 118,
        "Ice cream" : 2250,
        "Milk chocolate": 1680,
        "Doughnut" : 1075,
        "Pancake" : 80
    }

    global total_income
    total_income = sum(earings.values())

    print("Earned amount:")
    for item, income in earings.items():
        print(f"{item} : ${income}")
    print()
    print(f"Income: ${total_income:.1f}")

def calculate_expenses():
    staff_expenses = int(input("Staff expenses:"))
    other_expenses = int(input("Other expenses"))

    expenses = staff_expenses + other_expenses

    global total_income
    total_income -= expenses
    print(f"Net income: ${total_income:.1f}")
