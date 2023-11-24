# data preparation
import os

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "2"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

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

from simpletransformers.classification import ClassificationModel, ClassificationArgs

setup = {
    "model": "classla/xlm-r-bertic",
    "lr": "8e-6",
    "epoch": "15",
}


MODEL = setup["model"]
model_args = ClassificationArgs(
    num_train_epochs=int(setup["epoch"]),
    train_batch_size=32,
    learning_rate=float(setup["lr"]),
    overwrite_output_dir=True,
    regression=True,
    eval_batch_size=16,
    use_multiprocessing=False,
    use_multiprocessing_for_evaluation=False,
)
model = ClassificationModel(
    "xlmroberta",
    setup["model"],
    num_labels=1,
    args=model_args,
    use_cuda=True,
)
print("Starting training")
train_df = pd.DataFrame({"text": train_sentences, "labels": train_labels})
model.train_model(train_df)
print("Training finished")
predictions, raw_outputs = model.predict(test_sentences)


from sklearn.metrics import r2_score

result_dict = {
    "system": MODEL,
    "r2_score": r2_score(test_labels, predictions),
    "predictions": [
        {
            "train": "ParlaSent_BCS.jsonl",
            "test": "ParlaSent_BCS_test.jsonl",
            "predictions": predictions.tolist(),
        }
    ],
    **setup
}

with open("xlm-r-bertic.predictions.json", "w") as f:
    json.dump(result_dict, f)
