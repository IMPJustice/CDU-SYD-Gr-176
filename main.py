"""
    Github repo: https://github.com/IMPJustice/CDU-SYD-Gr-176.git
"""

from csv_to_txt import extract_csv_files
from top_30w_csv import count_words, save_top_words_to_csv
from top_30w_txt import count_tokens, save_top_tokens_to_txt
from scispacy_extract import extract_scispacy
from biobert_extract import extract_biobert
from comparison import compare

def main():
    #Task 1:Extract the ‘text’ in all the CSV files and store them into a single ‘.txt file’.
    
    csv_files = ['CSV1.csv', 'CSV2.csv','CSV3.csv','CSV4.csv']
    
    #Output file
    output_file = "result.txt"
    
    #Extract text from CSV files
    extract_csv_files(csv_files, output_file)
    
    '''
    Task 2:
        Install the libraries(SpaCy – scispaCy – ‘en_core_sci_sm’/’en_ner_bc5cdr_md’). 
        Install the libraries (Transformers (Hugging Face) - and any bio-medical model (BioBert) that can detect drugs, diseases, etc from the text). 
    '''
    #Answer:    pip install spacy scispacy
    #           pip install hugging-py-face
    #           pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_sm-0.5.4.tar.gz
    #           pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_ner_bc5cdr_md-0.5.4.tar.gz
    #           pip install transformers torch
    
    #Task 3.1:
    # Output CSV file to save the top 30 words and their counts
    output_csv = "top_30_words.csv"
    
    # Count words and get top 30
    top_30_words = count_words(output_file)
    
    # Save the top 30 words to a CSV file
    save_top_words_to_csv(top_30_words, output_csv)
    
    
    #Task 3.2:
    # Output file to save results
    output_txt = "top_30_tokens.txt"
    
    # Count unique tokens and get top 30
    top_30_token = count_tokens(output_file)
    
    # Save the top tokens to a file
    save_top_tokens_to_txt(top_30_token, output_txt)

    #Task 4:
    with open(output_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Extract using SciSpaCy 'en_core_sci_sm'
    scispacy_diseases_sm, scispacy_drugs_sm = extract_scispacy(text, chunk_size=100000, model_name="en_core_sci_sm")

    # Extract using SciSpaCy 'en_ner_bc5cdr_md'
    scispacy_diseases_bc5cdr, scispacy_drugs_bc5cdr = extract_scispacy(text, chunk_size=100000, model_name="en_ner_bc5cdr_md")

    # Extract using BioBERT
    biobert_diseases, biobert_drugs = extract_biobert(text, chunk_size=512)

    # Compare results between SciSpaCy (en_core_sci_sm) and BioBERT
    comparison_sci_sm_biobert = compare((scispacy_diseases_sm, scispacy_drugs_sm), (biobert_diseases, biobert_drugs))

    # Compare results between SciSpaCy (en_ner_bc5cdr_md) and BioBERT
    comparison_bc5cdr_biobert = compare((scispacy_diseases_bc5cdr, scispacy_drugs_bc5cdr), (biobert_diseases, biobert_drugs))

    # Print the comparison results
    print("\n--- Comparison between 'en_core_sci_sm' and BioBERT ---")
    print(f"Total Entities Detected by SciSpaCy: {comparison_sci_sm_biobert['total_scispacy']}")
    print(f"Total Entities Detected by BioBERT: {comparison_sci_sm_biobert['total_biobert']}")
    print(f"Common Diseases: {comparison_sci_sm_biobert['common_diseases']}")
    print(f"Common Drugs: {comparison_sci_sm_biobert['common_drugs']}")
    print(f"Different Diseases: {comparison_sci_sm_biobert['diff_diseases']}")
    print(f"Different Drugs: {comparison_sci_sm_biobert['diff_drugs']}")
    
    print("\n--- Comparison between 'en_ner_bc5cdr_md' and BioBERT ---")
    print(f"Total Entities Detected by SciSpaCy: {comparison_bc5cdr_biobert['total_scispacy']}")
    print(f"Total Entities Detected by BioBERT: {comparison_bc5cdr_biobert['total_biobert']}")
    print(f"Common Diseases: {comparison_bc5cdr_biobert['common_diseases']}")
    print(f"Common Drugs: {comparison_bc5cdr_biobert['common_drugs']}")
    print(f"Different Diseases: {comparison_bc5cdr_biobert['diff_diseases']}")
    print(f"Different Drugs: {comparison_bc5cdr_biobert['diff_drugs']}")

    
if __name__ == "__main__":
    main()