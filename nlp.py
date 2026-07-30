#!/usr/bin/env python


# file: nlp.py
# descr: natural language processing toolkit



import nltk 

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")


sentence = input("Enter a sentence: ")

words = nltk.word_tokenize(sentence)
print("Tokens:", words)

tags = nltk.pos_tag(words)
print("POS Tags:", tags)
