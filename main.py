import os
from top_30_words import count_tokens, words_to_csv

def main():
    #Prompt the user for the input .txt file path and convert path to the raw string
    file_path = r"{}".format(input("Enter the full path of the .txt file to process: "))
    #Remove double quotes
    file_path = file_path.strip('\"')

    #Task 3.1: Count word occurrences and save to CSV
    output_csv = 'top_30_words.csv'
    try:
        words_to_csv(file_path, output_csv)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")


    #Task 3.2: Count unique tokens using AutoTokenizer
    output_txt = 'top_30_tokens.txt'
    try:
        count_tokens(file_path, output_txt,1024)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
