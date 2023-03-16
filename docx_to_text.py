# functional

import os
import docx2txt

# Define the path to your folder containing the DOCX files
path = "c:/Users/ityle/Desktop/resumesround1/"

# Create a new directory to store the output text files
output_path = os.path.join(path)
if not os.path.exists(output_path):
    os.mkdir(output_path)

# Loop through each file in the folder and try to convert it to text
for filename in os.listdir(path):
    if filename.endswith(".docx"):
        try:
            # Convert the DOCX file to text
            text = docx2txt.process(os.path.join(path, filename))
            # Remove special characters and replace with underscores
            filename_text = "".join(x if x.isalnum() or x.isspace() else "_" for x in filename)
            # Save text to file in the output directory
            with open(os.path.join(output_path, f"{filename_text}.txt"), "w", encoding="utf-8") as text_file:
                text_file.write(text)
        except Exception as e:
            print(f"Error processing {filename}: {e}")
