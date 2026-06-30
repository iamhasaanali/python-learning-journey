def calculate_tip(bill):
    tip = bill / 10
    return tip
def calculate_total(bill):
    tip= calculate_tip(bill)
    total = bill +  tip
    return total
def print_receipt(bill):
    tip = calculate_tip(bill)
    total = calculate_total(bill)
    print("---Receipt---")
    print("Bill: ",bill)
    print("Tip (10%): ",tip)
    print("Total: ",total)
print_receipt(50)