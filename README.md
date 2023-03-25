# bulk_resumes with simple inputs and outputs, for data analysts
python scripts to help manage bulk pdf and docx resumes

-- pre-processing

0. remove duplicate files, if you download the file twice
https://github.com/MassiveNoobie/bulk_resumes/blob/main/delete_dupe_resumes.py

-- remove design, errors, and only manage data in txt files
1. turn pdf files into txt
-https://github.com/MassiveNoobie/bulk_resumes/blob/main/pdf_to_text.py
2. turn docx files into txt
-https://github.com/MassiveNoobie/bulk_resumes/blob/main/docx_to_text.py


-- NLP, Word Usage w/ csv outputs

3. tuh monthers . py - file name, file size, sentiment, POS/NER, word, count of words

https://github.com/MassiveNoobie/bulk_resumes/blob/main/tuh_monster.py
  -  Find POS and NER terms will automatically skip punctuations, dates, and numbers
  -  Labeling if the word/term is a POS (part of speech) or NER (named entity recognition) then occurences
  -  More on NER - https://youtu.be/oUDOemS61Co
  -  More on POS - https://youtu.be/LrLeVsLWZCQ
4. tiny critter . py - file name, word, count of words

https://github.com/MassiveNoobie/bulk_resumes/blob/main/tiny_critter.py
  -  Filter/Remove stop words with NLTK
  -  Filter/Remove punctuations, dates, and numbers

-- visualize

5. plugin csv files into visualization software
