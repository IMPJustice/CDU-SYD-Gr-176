counter = 0
total = 0  # Initialize total, if not done earlier

# Loop until the counter reaches 5
while counter < 5:
    if total < 13:
        total += 1  # Increase total if less than 13
    elif total > 13:
        total -= 1  # Decrease total if greater than 13
    else:
        counter += 2  # Increase counter by 2 only when total equals 13 (to avoid infinite loop)
    print(f"Total: {total}, Counter:{counter}")