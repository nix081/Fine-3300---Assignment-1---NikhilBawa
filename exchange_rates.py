"Fine 3300 Assignment 1 - Part 2: Exchange Rates"
"------------------------------------------------------"
""" 
Client would like to create a currency converter

They have provided the latest exchange rates to use

The user will be providing the amount to convert as well as the which currency to convert from (usd or cad)

Assumes values have been validated

Assumes only the file provided will be used as the USD/CAD Data Set

"""
"--------------------------------------------------------"

import csv

class ExchangeRates:
    def __init__(self, filename):
        self.__filename = filename
    #intialize the class
    #store the CSV file name, once the name is set ensure only that file is used to pull data
    
    def __pull_USDCAD_rate(self):
        
        exchange_data = open(self.__filename) #opens CSV file
        csv_data = csv.reader(exchange_data) #reads the data in the file
        data_lines = list(csv_data) #converts it to a python list, ensuring we can work with the information 

        usd_cad_rate = float(data_lines[-1][25]) # pulls the last rate (latest) from the USD/CAD coloumn of the CSV

        #stores the latest rate

        exchange_data.close() #closes the CSV file 

        return usd_cad_rate
    
    #private as user does not need to call this

    
    def convert(self, amount, from_currency, to_currency,):
        self.__from_currency = from_currency
        self.__to_currency = to_currency 
        rate = self.__pull_USDCAD_rate()
        if from_currency == "USD":
            return round((amount * rate),2)
        else:
            return round((amount/rate),2)
    #public method as this is the one the user directly uses
    #takes in the amount, from currency and to currency (provided via the user)
    #uses the internal function __pull_USDCAD_rate to get the latest rate 
    #returns the converted currency 
        
if __name__ == "__main__":
    print("USD/CAD Currency Converter")
    from_currency = str(input("Will you be converting from USD or CAD: ")).upper()
    #prompts user to pick the which currency to convert from 
    #since we are only working with USD and CAD, assuming the user is not using this to convert the same currency 
    #by default the other currency (cad or usd) is set as to_currency 
    if from_currency == "USD":
        to_currency = "CAD"
    else:
        to_currency = "USD"

    amount = float(input("Please enter the amount you will convert: "))
    #prompts user to provide the amount we need to convert
    conversion = ExchangeRates('BankOfCanadaExchangeRates.csv')
    #call the class, and provide the data set 
    result = conversion.convert(amount, from_currency, to_currency)
    #use convert function to convert the amount

    print(amount, from_currency, "is", result, to_currency)


        




