from dca_simulator import DCASimulator

def main():
    simulator = DCASimulator(
        price_data_path='data/sample_prices.csv',
        investment_amount=100,
        frequency_days=7
    )
    simulator.run()
    simulator.print_summary()

if __name__ == "__main__":
    main()
