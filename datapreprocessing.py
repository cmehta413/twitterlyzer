import pandas as pd
from nltk.corpus import stopwords
import string

# loading into memory
def load_doc(filename):
    # read-only file
    file = open(filename, 'r')
    # read text
    text = pd.read_csv("/Users/anishmeka/Desktop/CS196/Team_21/Project6500.csv", encoding = 'latin1')
    array = []
    for sentence in text['headline']:
        array.append(sentence)
    # close file
    file.close()
    return array

# turn doc into clean tokens
def clean_doc(doc):
    # use white space to split into tokens
    # doc = open(doc, 'w')
    tokens = doc.split(" ")
    # remove punctuation from each token
    table = str.maketrans('', '', string.punctuation)
    tokens = [w.translate(table) for w in tokens]
    # remove tokens that aren't part of the alphabet
    tokens = [word for word in tokens if word.isalpha()]
    # filter out stop words
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if not w in stop_words]
    # filter out short tokens
    tokens = [word for word in tokens if len(word) > 1]
    return tokens

# add doc to vocab after loading
def add_doc_to_vocab(filename, vocab):
    # load doc
    doc = load_doc(filename)
    # clean doc
    for sentence in doc:
        tmp = clean_doc(sentence)
        vocab.append(tmp)
    print(vocab)
# define vocab
vocab = []
# add doc to vocab
filename = '/Users/anishmeka/Desktop/CS196/Team_21/Project6500.csv'
add_doc_to_vocab(filename, vocab)
print(len(vocab))
