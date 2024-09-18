total = 0
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j  # Correct addition
        else:
            total += i - j  # Fixed subtraction (it should add the difference)
print(f"Total after loop: {total}")  # Output will help in revealing the key