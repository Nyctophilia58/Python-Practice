import re

text = "Five fantastic fish flew off to find faraway functions. Maybe find another fantastic fish? find my fish with a function please!"
result = re.sub(r'[\.\?\!\,\;\"]','',text)
print(result)

from nltk.corpus import stopwords

# define set of English stopwords
stop_words = set(stopwords.words('english'))

# remove stopwords from tokens in dataset
statement_no_stop = [word for word in word_tokens if word not in stop_words]