import nltk
import re
nltk.download('words', quiet=True)
nltk.download('names', quiet=True)
from nltk.corpus import words, names
word_list = words.words()
name_list = names.words()
word_list_orginal = words.words()

import string
alephbet = string.ascii_uppercase 
def encrypt(sent, key): 
    after_enc = ""
    sent_len = len(sent)
    for i in range(sent_len):
        char = sent[i] 
        if  not(char.islower() or  char.isupper()):
            after_enc += char
            continue
        if char.islower():
            idx = alephbet.index(char.upper()) 
            new_idx = (idx + key) % 26 
            after_enc += alephbet[new_idx].lower()
        else:
            idx = alephbet.index(char) 
            new_idx = (idx + key) % 26 
            after_enc += alephbet[new_idx]

    return after_enc

def decrypt(str, key):
    return encrypt(str, - key)

def crack(tar):
    parse_in = 0
    for i in range(len(tar.split())*26):
        candidate_dec = decrypt(tar, i)
        word_count = is_english_words(candidate_dec)
        perce = int(word_count / len(candidate_dec.split()) * 100)
        if perce > parse_in:
            parse_in = perce 
            decrypt_word = candidate_dec
    return decrypt_word

nltk.download('words')
english_words = nltk.corpus.words.words()

nltk.download('words')
english_words = nltk.corpus.words.words()
def is_english_words(sent):
    new_word = sent.split()
    count = 0
    for i in new_word:
        if i in english_words or i.lower() in english_words or i.upper() in english_words:
            count += 1
    return count
if __name__ == '__main__':
    a = encrypt('I live in Ramtha',13)
    print(a)