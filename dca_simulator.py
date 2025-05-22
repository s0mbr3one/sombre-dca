import pandas as pd

class DCASimulator:
    def __init__(self, price_data_path, investment_amount, frequency_days):
        self.price_data_path = price_data_path
        self.investment_amount = investment_amount
        self.frequency_days = frequency_days
        self.data = pd.read_csv(price_data_path, parse_dates=['date'])
        self.data.sort_values('date', inplace=True)
        self.investments = []

    def run(self):
        total_crypto = 0
        total_invested = 0
        for i in range(0, len(self.data), self.frequency_days):
            row = self.data.iloc[i]
            price = row['price']
            date = row['date']
            crypto_bought = self.investment_amount / price
            total_crypto += crypto_bought
            total_invested += self.investment_amount
            self.investments.append((date, price, crypto_bought))

        self.total_crypto = total_crypto
        self.total_invested = total_invested
        self.final_price = self.data.iloc[-1]['price']
        self.final_value = self.total_crypto * self.final_price

    def print_summary(self):
        print(f"Total invested: ${self.total_invested:.2f}")
        print(f"Total crypto accumulated: {self.total_crypto:.6f}")
        print(f"Final crypto value: ${self.final_value:.2f}")
        print(f"Net gain/loss: ${self.final_value - self.total_invested:.2f}")
