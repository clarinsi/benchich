import json
import pandas as pd
import os
from sklearn.dummy import DummyClassifier
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import ComplementNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import sklearn.feature_extraction


# Get all the datasets in the data/datasets directory
absolute_path = os.getcwd()
dataset_path = absolute_path[:-len("systems/dummy")] + "data/datasets/"

datasets = os.listdir(dataset_path)

# Add the path to the datasets
dataset_paths = [dataset_path + x for x in datasets]

dataset_dict = {x[0]:x[1] for x in list(zip(dataset_paths, datasets))}

for dataset_path in dataset_paths:
    # Load the json file
    with open(dataset_path, "r") as file:
        json_dict = json.load(file)

    dataset_name = dataset_dict[dataset_path]

    # Open the train, eval and test dictionaries as DataFrames
    train_df = pd.DataFrame(json_dict["train"])
    test_df = pd.DataFrame(json_dict["test"])
    dev_df = pd.DataFrame(json_dict["dev"])

    print(train_df.shape, test_df.shape, dev_df.shape)
    print(train_df.head())

    # Create X_train and Y_train parts, used for sci kit learning
    # List of texts in training split
    X_train = list(train_df.words)
    # List of labels in training split
    Y_train = list(train_df.labels)

    # List of texts in test split
    X_test = list(test_df.words)
    # List of labels in test split
    Y_test = list(test_df.labels)

    print(len(X_train), len(Y_train), len(X_test), len(Y_test))

    # Create a list of labels
    labels = list(train_df.labels.unique())
    print("Labels: {}".format(labels))

    # Create a TF-IDF representation of the text
    def data_iterator(f):
        for token in f:
            yield token

    def tokenizer(txt):
        """Simple whitespace tokenizer"""
        return txt.split()

    iterator=data_iterator(X_train)
    test_iterator=data_iterator(X_test)

    vectorizer=sklearn.feature_extraction.text.TfidfVectorizer(tokenizer=tokenizer,use_idf=True,min_df=0.005)

    d=vectorizer.fit_transform(iterator)

    d_test=vectorizer.transform(test_iterator)

    
    # Create a pipeline of models that you want to try:

    pipelines=[]

    model_dict = {"Dummy": DummyClassifier(strategy="stratified"), "Naive Bayes": ComplementNB(), "Logistic Regression": LogisticRegression(penalty=None)}#, "SVM": SVC(kernel="linear", C=2)}

    for model, model_name in list(zip(list(model_dict.values()),list(model_dict.keys()))):
        pipeline=make_pipeline(model)

        # Train the model
        pipeline.fit(d, Y_train)

        # Evaluate the model
        y_pred=list(pipeline.predict(d_test))

        # Create a json with results
        current_results = {
            "system": model_name,
            "predictions": [
                {
                "train": "{} (train split)".format(dataset_name),
                "test": "{} (test split)".format(dataset_name),
                "predictions": y_pred,
                }
            ],
            #"model": model_type_dict[model][1],
            #"args": model_args,
            }

        # Save the results as a new json
        with open("submissions/submission-{}-{}.json".format(model, dataset_name), "w") as file:
            json.dump(current_results, file)

        print("Classification with {} on {} finished.".format(model, dataset_name))
