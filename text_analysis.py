from collections import Counter
import numpy as np

import ast

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = open('temp.txt').read()
text = ast.literal_eval(text)

dickensizer = TfidfVectorizer()
tfidf_matrix = dickensizer.fit_transform(text)
val = np.argmax(np.array(cosine_similarity(dickensizer.transform(['excsue me but I must leave right now']), tfidf_matrix)[0]))

print text[val]
print text[val+1]
