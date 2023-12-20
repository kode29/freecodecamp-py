def main():
    print("This is a monthly payment loan calculator")
    print("")
    
    principal = float(input("Loan Amount: "))
    apr = float(input("Annual Percentage Rate: "))
    years = int(input("Number of Years: "))
    
    
    # 12 months * 100 (percent)
    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
      
    monthly_payment = principal * monthly_interest_rate / (1-(1+monthly_interest_rate) ** (-amount_of_months))
        
    # %.2f formats to 2 decimal places,seperated by the modulo operator (%) and the replacement variable
    print("Monthly Payment: $%.2f" % monthly_payment)
    
main()