import os
from top_30_words import top_30_words

# Dir path (Need to be dynamically)
input_directory = r'C:\Users\energ\Desktop\Hoang Phuc Huy Nguyen _ S _ Jay\Python\Assignment 2\Assignment_Material'
output_directory = r'C:\Users\energ\Desktop\Hoang Phuc Huy Nguyen _ S _ Jay\Python\Assignment 2\CSV_Output'

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

# Process each text file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(input_directory, filename)
        csv_filename = os.path.splitext(filename)[0] + '_top_30_words.csv'
        csv_path = os.path.join(output_directory, csv_filename)
        
        # Call the function to process the text file and save results to CSV
        top_30_words(file_path, csv_path)