# functional

import os
import hashlib

# function to get the hash value of a file
def get_hash(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
        return hashlib.md5(data).hexdigest()

# specify the directory path
directory = 'c:/Users/ityle/Desktop/resumesround1'

# create two dictionaries to store the hash values and filenames of PDF and Word files
pdf_dict = {}
word_dict = {}

# loop through all the files in the directory
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath):
        # check if the file is a PDF or Word file
        if filename.lower().endswith('.pdf'):
            # get the hash value of the file
            file_hash = get_hash(filepath)
            # check if the hash value already exists in the dictionary
            if file_hash in pdf_dict.values():
                # if the hash value already exists, delete the file
                os.remove(filepath)
            else:
                # if the hash value does not exist, add it to the dictionary
                pdf_dict[filename] = file_hash
        elif filename.lower().endswith('.doc') or filename.lower().endswith('.docx'):
            file_hash = get_hash(filepath)
            if file_hash in word_dict.values():
                os.remove(filepath)
            else:
                word_dict[filename] = file_hash
