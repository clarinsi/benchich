import json
import pandas as pd
import os
from sklearn.dummy import DummyClassifier


# Get all the datasets in the data/datasets directory
absolute_path = os.getcwd()
dataset_path = absolute_path[:-len("systems/dummy-classifier")] + "data/datasets/"

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

    for strategy in ["stratified", "most_frequent"]:
        model = f"dummy-{strategy}"

        dummy_mf = DummyClassifier(strategy=strategy)

        # Train the model
        dummy_mf.fit(X_train, Y_train)

        #Get the predictions
        y_pred_mf = dummy_mf.predict(X_test)

        y_pred = list(y_pred_mf)

        # Create a json with results
        current_results = {
            "system": model,
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
