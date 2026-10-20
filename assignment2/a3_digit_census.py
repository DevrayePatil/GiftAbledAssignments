num = int(input("Enter a number: "))

zeros = 0
odds = 0
evens = 0


while num > 0:
    digit = num % 10
    if digit == 0:
        zeros += 1
    elif digit % 2 == 0:
        evens += 1
    else:
        odds += 1
    num //= 10

print(f"Zeros: {zeros}, Odds: {odds}, Evens: {evens}")