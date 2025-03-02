import csv

def load_currency_rates(filename):
    currency_rates = {}
    with open(filename, mode='r', encoding='utf-8-sig', errors='replace') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if len(row) < 3:  # Skip invalid rows
                continue
            currency = row[0].strip()  # Extract currency code
            rate_str = row[2].strip()  # Extract exchange rate

            try:
                currency_rates[currency] = float(rate_str)
            except ValueError:
                print(f"Skipping invalid rate for {currency}: {rate_str}")
    
    return currency_rates

def convert_currency(amount, currency, rates):
    currency = currency.strip().upper()  # Normalize input
    return amount * rates.get(currency, None)

def main():
    filename = r"C:\\Users\\John Arvin\\Downloads\\TECHNICALS\\currency.csv"
    rates = load_currency_rates(filename)
    
    try:
        dollar_amount = int(input("How much dollar do you have? "))
        target_currency = input("What currency you want to have? ").strip().upper()

        converted_amount = convert_currency(dollar_amount, target_currency, rates)

        if converted_amount is not None:
            print(f"\nDollar: {dollar_amount} USD")
            print(f"{target_currency}: {converted_amount}")
        else:
            print("Currency not found in the exchange list.")
    
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
