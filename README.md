## Fine Assingment 1 By Nikhil Bawa 

This project has two parts and showcases two separate python classes:
  1. Mortgage Payment Calculator: Calculates mortgage payment for different payment frequencies based on the Canadian fixed-rate
  - This Calculator calculates 6 payments options:
      - Monthly
      - Semi-monthly
      - Bi-weekly
      - Weekly
      - Rapid bi-weekly
      - Rapid weekly
  - It converts the quoted rates to appropriate periodic rates for each respective period
  - Uses the PVA (present value of annuity) formula to calculate the payments for each period

  2. Exchange Rate Conversion Converts any amount between USD and CAD using the latest exchange rate provides in file called: BankOfCanadaExchangeRates.csv
  - This class wil read the file BankOfCanadaExchangeRates.csv
  - Extracts the most recent USD/CAD rate and converts them according to the nearest penny

## How to Run
### MortgagePayment
Run:
``` 
python mortgage_payment.py
```
You will be prompted to enter 
Interest Rate
Principal Amount 
Amortization

With the following inputs the output should be something like the following:
```
Mortgage Calculator
Please input your quoted interest rate: 5.5
Please input your principal amount: 100000
Please input your amortization period in years: 25

Output:
Here are calculated payments:
Monthly Payment: 610.39
Semi-Monthly Payment: 304.85
Bi-Weekly Payment: 281.38
Weekly Payment: 140.61
Rapid Bi-Weekly Payment: 305.2
Rapid Weekly Payment: 152.6
```

### Exchange Rate
```
python exchange_rates.py
```
Your will be prompted to enter:
Currency to convert from (USD or CAD)
Amount to Convert

With the following inputs the output should be something the like following:
```
Will you be converting from USD or CAD: CAD
Please enter the amount you will convert: 100000

Output:
100000.0 CAD is 73003.36 USD
```
