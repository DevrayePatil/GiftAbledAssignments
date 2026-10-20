print("Enter 3 favorite dices:")

dices = []
for i in range(3):
    dice = input(f"Dice {i + 1}: ")
    dices.append(dice)

print("Your favorite dices are:")
for dice in dices:
    print(dice, end=", ")