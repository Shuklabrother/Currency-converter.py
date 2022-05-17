from forex_python.converter import CurrencyRates
c = CurrencyRates()
Amount = float (input("Enter Amount:"))
print(c.convert('USD', 'INR', Amount))