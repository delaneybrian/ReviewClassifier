from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import numpy as np

def create_tfidf_representation(cleaned_data_list):

    review_classes = []
    review_text = []

    for cleaned_data in cleaned_data_list:
        review_text.append(cleaned_data["review_text"])
        review_classes.append(cleaned_data["review_class"])

    tfidf = TfidfVectorizer(preprocessor=' '.join, stop_words='english')

    y = np.array(review_classes)
    X = tfidf.fit_transform(review_text).toarray()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print(accuracy_score(y_test, y_pred))

def dummy_fun(doc):
    return doc