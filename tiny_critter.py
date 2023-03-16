import os
import csv
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from datetime import datetime

# Set the path to the directory containing the text files
path = "c:/Users/ityle/Desktop/resumesround1"

# Define a list of punctuations to filter out
punctuations = string.punctuation

# Define a function to check if a string is a valid date
def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d') and datetime.strptime(date_string, '%Y/%m/%d') and datetime.strptime(date_string, '%Y/%m')and datetime.strptime(date_string, 'MM/YYYY')
        return True
    except ValueError:
        return False

# Define a function to check if a string is a number
def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

# Create an empty dictionary to hold the word counts for each file
word_counts = {}

# Loop through each file in the directory
for file_name in os.listdir(path):
    if file_name.endswith(".txt"):
        # Read the contents of the file into a string
        with open(os.path.join(path, file_name), 'r', encoding='utf-8') as file:
            text = file.read()

        # Tokenize the text into individual words
        words = word_tokenize(text)

        # Remove stop words using NLTK
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word.lower() not in stop_words]

        # Filter out punctuations, dates, and numbers
        words = [word for word in words if word not in punctuations and not is_valid_date(word) and not is_number(word)]

        # Count the occurrences of each word in the file
        for word in words:
            if file_name in word_counts:
                if word in word_counts[file_name]:
                    word_counts[file_name][word] += 1
                else:
                    word_counts[file_name][word] = 1
            else:
                word_counts[file_name] = {word: 1}

# Write the results to a CSV file
with open('c:/Users/ityle/Desktop/resumesround1/word_counts.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["file name", "word", "count of word"])
    for file_name in word_counts:
        for word in word_counts[file_name]:
            writer.writerow([file_name, word, word_counts[file_name][word]])
