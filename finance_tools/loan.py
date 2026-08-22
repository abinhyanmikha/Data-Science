def calc_emi():
    amount=int(input("enter the loan amount"))
    annual_rate=int(input("enter the annual interest rate"))
    loan_tenure=int(input("enter the loan tenure (year)"))
    months=loan_tenure*12
    r=annual_rate/(12*100)
    return (amount*r*(1+r)**months)/((1+r)**months-1)

