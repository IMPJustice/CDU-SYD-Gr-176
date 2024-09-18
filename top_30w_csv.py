import re
import csv
from collections import Counter


def count_words(file):
    #Open the text file and read 
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read()

    #Convert to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())
    
    #Split the text into words
    words = text.split()

    #Count the occurrences 
    word_count = Counter(words)

    #Get the top 30 most common words
    top_30 = word_count.most_common(30)

    return top_30

def save_top_words_to_csv(top_words, output_csv):
    #Write the top 30 words and their counts to a CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Word", "Count"])
        writer.writerows(top_words)
    print(f"Top 30 words have been saved to {output_csv}")