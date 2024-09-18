from transformers import AutoTokenizer
from collections import Counter
import re

def count_tokens(file, model_name="bert-base-uncased", chunk_size=500000):
    #Load the AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    #Count occurrences 
    token_count = Counter()

    #Get the top 30 most common tokens
    with open(file, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            
            
            cleaned_chunk = remove_punctuation(chunk)

            # Tokenize the chunk
            tokens = tokenizer.tokenize(cleaned_chunk)

            # Update token counts
            token_count.update(tokens)

    # Get the top N most common tokens
    top_tokens = token_count.most_common(30)
    return top_tokens


def save_top_tokens_to_txt(top_tokens, output_file):
    try:
        #Save the top tokens to a file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("Top Word n Count:\n\n")
            for token, count in top_tokens:
                file.write(f"{token}: {count}\n")
        print(f"Top tokens have been saved to {output_file}")
    except Exception as e:
        print(f"Error writing to file: {e}")
        

def remove_punctuation(text):
    """
    Remove punctuation from the given text.
    """
    return re.sub(r'[^\w\s]', '', text)