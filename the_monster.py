import os
import csv
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Initialize NLTK resources
#nltk.download('vader_lexicon')
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')

# Set up sentiment analyzer and preprocessing tools
sia = SentimentIntensityAnalyzer()
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Define function to preprocess text and extract POS tags
def preprocess(text):
    tokens = word_tokenize(text)
    filtered_tokens = [lemmatizer.lemmatize(w.lower()) for w in tokens if w.lower() not in stop_words and w.isalnum()]
    pos_tags = nltk.pos_tag(filtered_tokens)
    return pos_tags

# Define function to get NER entities
def get_entities(text):
    entities = nltk.ne_chunk(nltk.pos_tag(word_tokenize(text)))
    return entities

# Define function to get sentiment score
def get_sentiment(text):
    sentiment = sia.polarity_scores(text)['compound']
    return sentiment

# Define function to process a single file and generate row data
def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:  # specify encoding
        text = f.read()
        filename = os.path.basename(filepath)
        filesize = os.path.getsize(filepath)
        sentiment_score = get_sentiment(text)
        pos_tags = preprocess(text)
        entities = get_entities(text)
        rows = []
        for term, pos in pos_tags:
            if pos.startswith('NN'):
                term_count = pos_tags.count((term, pos))
                rows.append([filename, filesize, sentiment_score, 'POS', term, term_count])
        for entity in entities:
            if hasattr(entity, 'label') and entity.label() in ['PERSON', 'ORGANIZATION', 'LOCATION']:
                entity_name = ' '.join([word for word, tag in entity.leaves()])
                entity_count = entities.count(entity)
                rows.append([filename, filesize, sentiment_score, 'NER', entity_name, entity_count])
        return rows


# Define function to process all files in a folder and export as CSV
def process_folder(folderpath, outputpath):
    rows = []
    for filename in os.listdir(folderpath):
        if filename.endswith('.txt'):
            filepath = os.path.join(folderpath, filename)
            file_rows = process_file(filepath)
            rows.extend(file_rows)
    with open(outputpath, 'w', newline='', encoding='utf-8') as f:  # specify encoding
        writer = csv.writer(f)
        writer.writerow(['file name', 'file size', 'sentiment score', 'terms', 'count'])
        for row in rows:
            writer.writerow(row)


# Example usage: process a folder of text files in './data' and export results to './output.csv'
process_folder('c:/Users/ityle/Desktop/resumesround1/', 'c:/Users/ityle/Desktop/resumesround1/output.csv')
