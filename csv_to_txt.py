import pandas as pd

def extract_csv_files(files, output_file):
    with open(output_file, 'w', encoding='utf-8') as f_output:
        for file in files:
            print(f"Processing file: {file}")
            
            #Read the CSV file
            df = pd.read_csv(file)
            
            #Write a header
            f_output.write(f"\n--- Contents of {file} ---\n\n")
            
            #Convert and write it to the output file
            df_as_string = df.to_string(index=False)
            f_output.write(df_as_string + "\n")
    
    print(f"All content from CSV files has been extracted to {output_file}")