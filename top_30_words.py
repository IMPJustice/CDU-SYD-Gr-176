import csv
from collections import Counter
import re
import os

def top_30_words (file_path, csv_path):

    # File check
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f'The file at {file_path} does not existed or not to be found')
    
    try:
        # Read the text file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except PermissionError as e:
        raise PermissionError(f"Permission denied: {e}")

    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text.lower())  # Convert to lowercase

    # Count the  word
    word_counts = Counter(words)

    # Find the top 30 most common words
    top_30_words = word_counts.most_common(30)

    # Write the results to a CSV file
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Count']) 
        writer.writerows(top_30_words) 


print(f"Successfully create CSV file.")
