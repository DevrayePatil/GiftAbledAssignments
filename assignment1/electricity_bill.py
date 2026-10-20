units = int(input("Enter the number of units consumed: "))

if units <= 100:
    bill_amount = units * 5
elif units <= 200:
    bill_amount = (100 * 5) + ((units - 100) * 7)
elif units <= 300:
    bill_amount = (100 * 5) + (100 * 7) + ((units - 200) * 10)
else:
    bill_amount = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 15)

print(f"The electricity bill amount is: Rs. {bill_amount:.2f}") 