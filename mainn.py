from forex_python.converter import CurrencyRates

c = CurrencyRates()

date_obj = (2024, 4, 15)

usd_to_rub = c.get_rate('USD', 'RUB')

print(f"Курс USD/RUB на 15.04.2024: {usd_to_rub:.2f}")
