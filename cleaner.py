import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

def setup_clean():
    nltk.download('punkt')
    nltk.download('stopwords')

def clean_text(raw_text):
    tokens = tokenise(raw_text)
    tokens = normalise(tokens)
    tokens = removeStopWords(tokens)
    tokens = stem(tokens)
    return tokens

def tokenise(rawtext):
    return nltk.word_tokenize(rawtext)

def normalise(tokens):
    normalised = []
    for token in tokens:
        normalised.append(token.lower())
    return normalised

def removeStopWords(tokens):
    stopwds = stopwords.words('english')
    removed = []
    [removed.append(token) for token in tokens if token not in stopwds]
    return removed

def stem(tokens):
    stemmed = []
    stemmer = PorterStemmer()
    [stemmed.append(stemmer.stem(word)) for word in tokens]
    return stemmed
