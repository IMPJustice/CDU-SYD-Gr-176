from transformers import AutoTokenizer
from collections import Counter
import re
import os
import csv


#Task 3.1
def words_to_csv (file_path, csv_path):

    #Check File
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f'The file at {file_path} does not existed or not to be found')
    
    try:
        #Read the text file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except PermissionError as e:
        raise PermissionError(f"Permission denied: {e}")

    #Tokenize text into words
    words = re.findall(r'\b\w+\b', text.lower())

    #Count the token
    word_counts = Counter(words)

    #List 30 common words
    top_30_words = word_counts.most_common(30)

    #Write the results to a CSV file
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Count']) 
        writer.writerows(top_30_words) 

    print(f"Successfully create CSV file.")
    

#Task 3.2
def count_tokens(file_path, txt_path, batch_size=1024):
    
    #Load pre-trained tokenizer
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

    #Check input file
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file at path {file_path} does not exist.")
    
    token_counts = Counter()

    try:
        #Read text file content
        with open(file_path, 'r', encoding='utf-8') as file:
            
            while True:
                text_chunk = file.read(batch_size)
                if not text_chunk:
                    break
                
                # Tokenize the chunk of text
                tokens = tokenizer.tokenize(text_chunk)

                # Filter out punctuation and non-word characters
                filtered_tokens = [token for token in tokens if re.match(r'^\w+$', token)]

                # Update token counts
                token_counts.update(filtered_tokens)
                
            
    except PermissionError as e:
        raise PermissionError(f"Permission denied: {e}")


    #List 30 most common words
    top_30_tokens = token_counts.most_common(30)

    #Save the results to the specified .txt file
    try:
        with open(txt_path, 'w', encoding='utf-8') as out_file:

            out_file.write("Top 30 tokens and their counts:\n")
            for token, count in top_30_tokens:
                out_file.write(f"{token}: {count}\n")
        print(f"Results saved to {file_path}")
        
    except PermissionError as e:
        raise PermissionError(f"Could not write the file: {e}")

    return top_30_tokens
