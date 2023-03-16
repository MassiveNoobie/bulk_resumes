# functional


import os
import PyPDF2

# Define the path to your folder containing the PDF files
path = "c:/Users/ityle/Desktop/resumesround1"

# Loop through each file in the folder and try to open it with PyPDF2
for filename in os.listdir(path):
    if filename.endswith(".pdf"):
        try:
            # Open the PDF file
            with open(os.path.join(path, filename), 'rb') as pdf_file:
                # Create a PDF reader object
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                # Check if the file is encrypted or has any errors
                text = ""
                for i in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[i]
                    text += page.extract_text()
                # Remove special characters and replace with underscores
                filename_text = "".join(x if x.isalnum() or x.isspace() else "_" for x in filename)
                # Save text to file
                with open(os.path.join(path, f"{filename_text}.txt"), "w", encoding="utf-8") as text_file:
                    text_file.write(text)
        except PyPDF2.utils.PdfReadError:
            print(filename + " is broken")
