# bulk_resumes with simple inputs and outputs so analysts of any level
python scripts to help manage bulk pdf and docx resumes

-- pre-processing

0. remove duplicate files, if you download the file twice

-- remove design, errors, and only manage data in txt files

1. turn pdf files into txt
2. turn docx files into txt

-- NLP, Word Usage w/ csv outputs

3. tuh monthers - file name, file size, sentiment, POS/NER, word, count of words
  -  Find POS and NER terms will automatically skip punctuations, dates, and numbers
  -  Labeling if the word/term is a POS (part of speech) or NER (named entity recognition) then occurences
  -  More on NER - https://youtu.be/oUDOemS61Co
  -  More on POS - https://youtu.be/LrLeVsLWZCQ
4. tiny critter - file name, word, count of words
  -  Filter/Remove stop words with NLTK
  -  Filter/Remove punctuations, dates, and numbers

-- visualize

5. plugin csv files into visualization software
