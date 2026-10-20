age = int(input("Enter your age: "))

ticket_price = 299

if age < 5:
   price = 0
   category = "free"
elif 5 <= age < 18:
    price = ticket_price * 0.5
    category = "half"
elif 18 <= age < 60:
    price = ticket_price 
    category = "full"
else:
    price = ticket_price * 0.7
    category = "concession"

print(f"The ticket price for a {category} category is: Rs. {price:.2f}")