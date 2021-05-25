"""from spam_data import training_spam_docs, training_doc_tokens, training_labels
from sklearn.naive_bayes import MultinomialNB
from preprocessing import preprocess_text

# Add your email text to test_text between the triple quotes:
test_text = """
"""Have you ever wondered how an email ends up in the spam folder? Or how customer service phone systems are able to understand what you're saying? From a cleaner inbox to faster customer service and virtual assistants that can tell you the weather, the number of applications using natural language processing (NLP) is rapidly growing. NLP is all about how computers work with human language. Learn how to create your own powerful NLP programs with this new course!
 
Start Now
 
Happy coding,
Codecademy"""
"""
test_tokens = preprocess_text(test_text)

def create_features_dictionary(document_tokens):
  features_dictionary = {}
  index = 0
  for token in document_tokens:
    if token not in features_dictionary:
      features_dictionary[token] = index
      index += 1
  return features_dictionary

def tokens_to_bow_vector(document_tokens, features_dictionary):
  bow_vector = [0] * len(features_dictionary)
  for token in document_tokens:
    if token in features_dictionary:
      feature_index = features_dictionary[token]
      bow_vector[feature_index] += 1
  return bow_vector

bow_sms_dictionary = create_features_dictionary(training_doc_tokens)
training_vectors = [tokens_to_bow_vector(training_doc, bow_sms_dictionary) for training_doc in training_spam_docs]
test_vectors = [tokens_to_bow_vector(test_tokens, bow_sms_dictionary)]

spam_classifier = MultinomialNB()
spam_classifier.fit(training_vectors, training_labels)

predictions = spam_classifier.predict(test_vectors)

print("Looks like a normal email!" if predictions[0] == 0 else "You've got spam!")"""


"""from preprocessing import preprocessed_text:

def text_to_bow(some_text):
    bow_dictionary = dict()
    tokens = preprocessed_text(some_text)
    for token in tokens:
        if token in bow_dictionary:
            bow_dictionary[token] += 1
        else:
            bow_dictionary[token] = 1
    return bow_dictionary

print(text_to_bow("I love fantastic flying fish. These flying fish are just ok, so maybe I will find another few fantastic fish..."))"""

"""from preprocessing import preprocess_text
# Define create_features_dictionary() below:
def create_features_dictionary(documents):
  features_dictionary = {}
  merged = " ".join(documents)
  tokens = preprocess_text(merged)
  index = 0
  for token in tokens:
    if token not in features_dictionary:
      features_dictionary[token] = index
      index += 1
  return features_dictionary, tokens

training_documents = ["Five fantastic fish flew off to find faraway functions.", "Maybe find another five fantastic fish?", "Find my fish with a function please!"]

print(create_features_dictionary(training_documents)[0])"""


from preprocessing import preprocess_text
# Define text_to_bow_vector() below:
def text_to_bow_vector(some_text, features_dictionary):
  bow_vector = [0] * len(features_dictionary)
  tokens = preprocess_text(some_text)
  for token in tokens:
    feature_index = features_dictionary[token]
    bow_vector[feature_index] += 1
  return bow_vector, tokens

features_dictionary = {'function': 8, 'please': 14, 'find': 6, 'five': 0, 'with': 12, 'fantastic': 1, 'my': 11, 'another': 10, 'a': 13, 'maybe': 9, 'to': 5, 'off': 4, 'faraway': 7, 'fish': 2, 'fly': 3}

text = "Another five fish find another faraway fish."
print(text_to_bow_vector(text, features_dictionary)[0])
