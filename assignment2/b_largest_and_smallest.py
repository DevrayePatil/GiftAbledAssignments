min = 101
max = -1

print("Enter marks between 0 and 100 :")

marks = []
for i in range(10):
    mark = int(input(f"Enter mark {i + 1}: "))

    marks.append(mark)

    if mark > max:
        max = mark
    if mark < min:
        min = mark

print(f"Maximum mark: {max}")
print(f"Minimum mark: {min}")
