import nltk
import numpy as np
import string
import warnings
warnings.filterwarnings("ignore")
# From scikit learn library, import the TFidf vectorizer to convert a collection of raw documents to a matrix of TF-IDF features.
from sklearn.feature_extraction.text import TfidfVectorizer
# Also, import cosine similarity module from scikit learn library
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('punkt')   # for first-time use only. Punkt is a Sentence Tokenizer
nltk.download('wordnet')    # for first-time use only. WordNet is a large lexical database of English.

f = open('content.txt','r',errors = 'ignore', encoding = 'utf-8')
paragraph = f.read()

sent_tokens = nltk.sent_tokenize(paragraph)
word_tokens = nltk.word_tokenize(paragraph)

# Lemmitization
lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]    # iterate through every token and lemmatize it
# string.punctuation has all the punctuations
# ord(punct) convert punctuation to its ASCII value
# dict contains {ASCII: None} for punctuation mark
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
# This will return the word to LemTokens after Word tokenize, lowering its case and removing punctuation mark
# translate will find punctuation mark in remove_punct_dict and if found replace it with None
def Normalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)   # Appending the Question user ask to sent_tokens to find the Tf-Idf and cosine_similarity between User query and the content.
    TfidfVec = TfidfVectorizer(tokenizer = Normalize, stop_words='english')    #tokenizer ask about Pre-processing parameter and it will consume the Normalize() function and it will also remove StopWords
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)     # It will do cosine_similarity between last vectors and all the vectors because last vector contain the User query
    idx = vals.argsort()[0][-2]     # argsort() will sort the tf_idf in ascending order. [-2] means second last index i.e. index of second highest value after sorting the cosine_similarity. Index of last element is not taken as query is added at end and it will have the cosine_similarity with itself.
    flat = vals.flatten()    # [[0,...,0.89,1]] -> [0,...,0.89,1] this will make a single list of vals which had list inside a list.
    flat.sort()
    req_tfidf = flat[-2]  # this contains tfid value of second highest cosine_similarity
    if(req_tfidf == 0):    # 0 means there is no similarity between the question and answer
        robo_response = robo_response + "I am sorry! I don't understand you. Please rephrase your query."
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]    # return the sentences at index -2 as answer
        return robo_response