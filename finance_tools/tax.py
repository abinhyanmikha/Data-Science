def calc_tax():
    amount=int(input("enter the amount"))
    tax=int(input("enter the tax rate"))
    total_tax_amt=amount*tax/100
    return total_tax_amt

