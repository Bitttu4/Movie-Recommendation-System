import ast
import pandas as pd
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L


def convert3(text):
    L = []
    counter = 0

    for i in ast.literal_eval(text):
        if counter != 3:
            L.append(i['name'])
            counter += 1
        else:
            break

    return L


def fetch_director(text):
    L = []

    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
            break

    return L


def stem(text):
    y = []

    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)