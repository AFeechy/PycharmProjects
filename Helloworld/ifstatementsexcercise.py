house_price = 1000000
good_credit = False

if good_credit:
    down_payment = 0.1 * house_price

else:
    print ("You have bad credit")
    down_payment = 0.2 * house_price
print(f"Down payment: ${down_payment}")