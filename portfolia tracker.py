stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = []
total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available stocks:", ", ".join(stocks.keys()))

while True:
    stock = input("Enter stock name (or 'done' to finish): ").strip().upper()

    if stock == "DONE":
        break

    if stock not in stocks:
        print("Stock not available. Please choose from the list.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    price = stocks[stock]
    investment = price * quantity
    total_investment += investment

    portfolio.append({
        "Stock": stock,
        "Price": price,
        "Quantity": quantity,
        "Investment": investment
    })

    print("Stock added successfully!")
    print("Investment:", investment)

print("\n===== YOUR PORTFOLIO =====")

if portfolio:
    for item in portfolio:
        print(
            item["Stock"],
            "| Price:", item["Price"],
            "| Quantity:", item["Quantity"],
            "| Investment:", item["Investment"]
        )

    print("Total investment:", total_investment)

    save = input("Save portfolio to CSV? (yes/no): ").strip().lower()

    if save == "yes":
        import csv

        with open("stock_portfolio.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["Stock", "Price", "Quantity", "Investment"]
            )
            writer.writeheader()
            writer.writerows(portfolio)
            writer.writerow({
                "Stock": "TOTAL",
                "Price": "",
                "Quantity": "",
                "Investment": total_investment
            })

        print("Portfolio saved to stock_portfolio.csv")
else:
    print("No stocks were added.")