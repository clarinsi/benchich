# A dummy script that will load train and test data and predict the average value every time.

import pandas as pd
import json

mapper = {
    "Negative": 0.0,
    "M_Negative": 1.0,
    "N_Neutral": 2.0,
    "P_Neutral": 3.0,
    "M_Positive": 4.0,
    "Positive": 5.0,
}

train = pd.read_json("../../data/ParlaSent_BCS.jsonl", lines=True)
train["reconciliation"] = [mapper.get(i) for i in train.reconciliation]
test = pd.read_json("../../data/ParlaSent_BCS_test.jsonl", lines=True)
test["annotator1"] = [mapper.get(i) for i in test.annotator1]

train_sentences = train.sentence.values.tolist()
train_labels = train.reconciliation.values.tolist()

test_sentences = test.sentence.values.tolist()
test_labels = test.annotator1.values.tolist()


# "Train"
value_to_return = sum(train_labels) / len(train_labels)

# "Evaluate"
predictions = [value_to_return for i in test_sentences]

result_dict = {
    "system": "Dummy (mean)",
    "predictions": [
        {
            "train": "ParlaSent_BCS.jsonl",
            "test": "ParlaSent_BCS_test.jsonl",
            "predictions": predictions,
        }
    ],
}

with open("dummy.predictions.json", "w") as f:
    json.dump(result_dict, f)
