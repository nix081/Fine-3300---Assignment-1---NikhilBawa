"Fine 3300 Assignment 1 - Part 1: Mortgage Calculator"
"------------------------------------------------------"
""" 
Client wants to calculate mortage payments for different payment options

The calculator should calculate the following:
monthly, semi-monthly, bi-weekly, weekly, rapid bi-weekly, and rapid weekly

It will be for fixed-rate mortgages at a semi-annually compounded rate

The user will provide the principal amount, the quoted rate, and the ammortization period 

Client would like the results to be returned as a tuple, so it cannot be changed after the calculation as been made and rounded

Assumes values have been validated

"""
"--------------------------------------------------------"

class MortgagePayment:

    __payment_options = {"monthly": 12, "semi-monthly": 24, "bi-weekly": 26, "weekly": 52}
    #kept payment_option private as the payment periods are fixed and dont need to be changed
    #ensures consistency

    def __init__(self, quoted_rate, amortization_period):
        self.__quoted_rate = float(quoted_rate)/100
        self.__amortization_period = int(amortization_period)
    #store the quoted rate as decimal and amortization period as integer
    # once user provides both they are privated so it cannot be changed in the further calculations

    def __periodic_int_rate(self, payment_period):
        payment_period = int(payment_period)
        semi_annual_rate = self.__quoted_rate / 2
        effective_rate = (1 + (semi_annual_rate))**2 - 1
        periodic_rate = (1 + effective_rate)**(1/payment_period) - 1
        return periodic_rate
    #this is an internal function used to change the quoted interest to the periodic interest rate
    #user does not directly call for this function so it kept private
    
    def __pva_factor(self, r, n):
        pva = (1 - (1 + r) ** (-n))/r
        return pva
    #another internatal function used to store the PVA formula which is used later to calculate the payment
    #used as a seperate function so it is easier to call later 

    def payments(self, principal_amt):
        results = {}
        for payment_type in self.__payment_options:
            period = self.__payment_options[payment_type] #uses dictionary to find number of payments as year corresponding with payment period
            r =  self.__periodic_int_rate(period) #calc the periodic rate for each period
            n = self.__amortization_period * period #calc the total number of periods
            results[payment_type] = principal_amt/self.__pva_factor(r,n) # calc the payments 

        monthly_payment = results["monthly"]
        semi_monthly_payment = results["semi-monthly"]
        biweekly_payment = results["bi-weekly"]
        weekly_payment = results["weekly"]
        rapid_bi_weekly = monthly_payment/2
        rapid_weekly = monthly_payment/4
    
        return ( round(monthly_payment, 2), round(semi_monthly_payment, 2), round(biweekly_payment, 2), round(weekly_payment, 2), round(rapid_bi_weekly, 2), round(rapid_weekly, 2))
    #public 
    #user uses this function to directly calculate the payments
    #the function calculates the payments are returns them as a tuple so is cannot be changed later

if __name__ == "__main__":
    print("Mortgage Calculator")
    #user gives the information necessary, all information is convereted to respective data type to ensure calculation remain valid
    quoted_rate = float(input("Please input your quoted interest rate: "))
    principal_amt = float(input("Please input your principal amount: "))
    amortization_period = int(input("Please input your amortization period in years: "))

    mortgage = MortgagePayment(quoted_rate, amortization_period)

    all_payments = mortgage.payments(principal_amt)

    print("Here are calculated payments:")

    print("Monthly Payment:", all_payments[0])
    print("Semi-Monthly Payment:", all_payments[1])
    print("Bi-Weekly Payment:", all_payments[2])
    print("Weekly Payment:", all_payments[3])
    print("Rapid Bi-Weekly Payment:", all_payments[4])
    print("Rapid Weekly Payment:", all_payments[5])
