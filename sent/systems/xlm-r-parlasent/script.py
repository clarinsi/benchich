# data preparation

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


# Predicting:

from transformers import (
    AutoModelForSequenceClassification,
    TextClassificationPipeline,
    AutoTokenizer,
    AutoConfig,
)

MODEL = "classla/xlm-r-parlasent"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

pipe = TextClassificationPipeline(
    model=model,
    tokenizer=tokenizer,
    return_all_scores=True,
    task="sentiment_analysis",
    device=2,
    function_to_apply="none",
)
predictions = pipe(test_sentences)
predictions = [i[0].get("score") for i in predictions]

from sklearn.metrics import r2_score

result_dict = {
    "system": MODEL,
    "r2_score": r2_score(test_labels, predictions),
    "predictions": [
        {
            "train": "ParlaSent_BCS.jsonl",
            "test": "ParlaSent_BCS_test.jsonl",
            "predictions": predictions,
        }
    ],
}

with open("xml-r-parlasent.predictions.json", "w") as f:
    json.dump(result_dict, f)
