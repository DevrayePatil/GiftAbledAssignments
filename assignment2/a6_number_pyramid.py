rows = int(input("Enter the number of rows for the triangle: "))

for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    numbers = ""

    for j in range(1, i + 1):
        numbers += str(j) + " "

    print(spaces + numbers.strip())
    