from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from pandas import *
import pickle
import sys

# Step 1: Data Preparation
# Assuming you have 'text' and 'label' columns in your dataset.
# Load your data into a pandas DataFrame or use any other data loading method.
# For this example, we'll use a simple list of reviews and labels.

filename = 'classifier.bin'


def train():
	data = read_csv("nofly.csv")
	text = data['text'].tolist()
	label = data['label'].tolist()
	# Step 2: Text Preprocessing and Feature Extraction
	vectorizer = CountVectorizer()
	X = vectorizer.fit_transform(text)
	# Step 4: Split Data
	X_train, X_test, y_train, y_test = train_test_split(X, label, test_size=0.2, random_state=42)

	# Step 5: Create and Train the Classifier
	classifier = MultinomialNB()
	classifier.fit(X_train, y_train)

	# Step 6: Evaluate the Classifier
	y_pred = classifier.predict(X_test)
	accuracy = accuracy_score(y_test, y_pred)
	report = classification_report(y_test, y_pred)

	print(f"Accuracy: {accuracy}")
	print("Classification Report:\n", report)
	# save the model to disk
	pickle.dump(classifier, open(filename, 'wb')) 
	pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))

def classify(text):
	classifier = pickle.load(open(filename, 'rb'))
	vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
	# New text you want to classify
	new_text = [text]

	# Preprocess and convert new text into numerical features using the same vectorizer
	new_text_features = vectorizer.transform(new_text)

	# Use the trained classifier to predict the label
	predicted_label = classifier.predict(new_text_features)
	return predicted_label[0]

	#print(f"Predicted Label: {predicted_label[0]}")

if __name__ == '__main__':
	train()
	classification = input("would you like to classify(Y/n)?\n")
	if classification.upper() == "Y":
		print(classify("generate an image of a cat"))
	else:
		pass
