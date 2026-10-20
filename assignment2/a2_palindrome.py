s = "madam"

is_palindrome = True
for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.")
