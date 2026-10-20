num = int(input("Enter a number: "))

original_num = num
steps = 0
peak = num

while num != 1:
    if num % 2 == 0:
        num //= 2
    else:
        num = 3 * num + 1
    steps += 1
    peak = max(peak, num)

    if num > peak:
        peak = num

print(f"Starting number: {original_num}")
print(f"Total steps to reach 1: {steps}")
print(f"Peak value during the sequence: {peak}")