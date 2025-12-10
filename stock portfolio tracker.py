# Hardcoded stock prices (you can add more)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 400
}

portfolio = {}  # To store user stocks and quantity

print("📈 Welcome to the Stock Portfolio Tracker!")
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

print("\nEnter 'done' when you finish adding stocks.\n")

# Taking user input
while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()

    if stock.lower() == "done":
        break

    if stock not in stock_prices:
        print("❌ Stock not available. Choose from the given list.\n")
        continue

    qty = int(input(f"Enter quantity of {stock}: "))

    portfolio[stock] = portfolio.get(stock, 0) + qty
    print("✔ Added!\n")

# Calculate total investment
total_value = 0
print("\n📊 Your Portfolio:")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_value += value
    print(f"{stock} - Qty: {qty}, Value: ${value}")

print("\n💰 Total Investment Value:", total_value)

# Optional: Save result
choice = input("\nDo you want to save this to a file? (yes/no): ").lower()

if choice == "yes":
    file_type = input("Save as txt or csv? ").lower()

    if file_type == "txt":
        with open("portfolio.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            for stock, qty in portfolio.items():
                value = qty * stock_prices[stock]
                f.write(f"{stock} - Qty: {qty}, Value: ${value}\n")
            f.write(f"\nTotal Investment: ${total_value}")
        print("📁 Saved as portfolio.txt")

    elif file_type == "csv":
        with open("portfolio.csv", "w") as f:
            f.write("Stock,Quantity,Value\n")
            for stock, qty in portfolio.items():
                value = qty * stock_prices[stock]
                f.write(f"{stock},{qty},{value}\n")
        print("📁 Saved as portfolio.csv")

    else:
        print("⚠ Invalid file type. Not saved.")

print("\n✔ Program finished.")