vowels = ["a", "e", "i", "o", "u"]

string = "This is a sample string to count vowels."


count = 0
for char in string.lower():
    if char in vowels:
        count += 1

print("Number of vowels in the string:", count)
