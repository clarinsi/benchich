# Named entity recognition benchmark for Croatian and Serbian

The purpose of this subrepo is gathering and comparison of results, obtained on named entity recognition (NER).

The benchmark consists of 4 datasets, manually-annotated with named entitites:
 - standard Croatian
 - non-standard Croatian
 - standard Serbian
 - non-standard Serbian

# Benchmark scores

Benchmark scores were calculated only once per system and might differ slightly your results. Finetuning hyperparameters are listed in the json files, where applicable.

## Standard Croatian

The models are tested on the test split of Croatian linguistic training corpus hr500k 2.0.

| system | train | micro F1 | macro F1 |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## Non-Standard Croatian

The models are tested on the test split of Croatian Twitter training corpus ReLDI-NormTagNER-hr 3.0.

| system | train | micro F1 | macro F1 |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## Standard Serbian

The models are tested on the test split of Serbian linguistic training corpus SETimes.SR 2.0.

| system | train | micro F1 | macro F1 |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## Non-Standard Serbian

The models are tested on the test split of Serbian Twitter training corpus ReLDI-NormTagNER-sr 3.0.

| system | train | micro F1 | macro F1 |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

# Data

The datasets used for benchmarking are:
- Croatian linguistic training corpus hr500k 2.0
- Croatian Twitter training corpus ReLDI-NormTagNER-hr 3.0
- Serbian linguistic training corpus SETimes.SR 2.0
- Serbian Twitter training corpus ReLDI-NormTagNER-sr 3.0

The datasets are available in the `data/datasets` directory.

They were prepared by:
1. first downloading the data from the CLARIN.SI repository with the `download_data.sh` script from the `data` directory. This downloads the Croatian and Serbian datasets in a new folder `datasets` inside the directory: ```bash prepare_datasets.sh "s_Croatian" "ns_Croatian" "s_Serbian" "ns_Serbian" > dataset_preparation.log```. You can use all available datasets or define just a couple of them as the arguments (e.g., if you want to download only standard and non-standard Serbian: "s_Serbian" "ns_Serbian")
2. then running [the prepared script](data/dataloader.py) from the `data` directory. This prepares the following files:

```
data
├── datasets
    ├── datasets/hr500k.conllup_extracted.json
    ├── datasets/reldi-normtagner-hr.conllup_extracted.json
    ├── datasets/set.sr.plus.conllup_extracted.json
    ├── datasets/reldi-normtagner-sr.conllup_extracted.json
```

The datasets are JSON files - dictionaries which consist of the following keys:
 - "labels" (list of NE labels used in the dataset)
 - "train", "dev", "test" (dataset splits)

"train", "dev", "test" are also dictionaries, with the following keys:
 - "sentence_id" (original sentence id)
 - "words" (word forms as they appear in the sentence)
 - "labels" (NE labels)


**Dataset sizes**

Dataset sizes in number of instances (words):

| hr500k (HR_s) | reldi-normtagner-hr (HR_ns) | reldi-normtagner-sr (SR_ns) | set.sr.plus (SR_s) |
|---------------|-----------------------------|-----------------------------|--------------------|
| 499,635       | 89,855                      | 97,673                      | 92,271             |


An example of how to use the prepared datasets with the simpletransformers library:
To use them for classification with the simpletransformers library:

```
import json
import pandas as pd

# Define the path to the dataset
dataset_path = "datasets/set.sr.plus.conllup_extracted.json"

# Load the json file
with open(dataset_path, "r") as file:
    json_dict = json.load(file)

# Open the train, eval and test dictionaries as DataFrames
train_df = pd.DataFrame(json_dict["train"])
test_df = pd.DataFrame(json_dict["test"])
dev_df = pd.DataFrame(json_dict["dev"])

# Change the sentence_ids to integers (!! important - otherwise, the models do not work)
test_df['sentence_id'] = pd.factorize(test_df['sentence_id'])[0]
train_df['sentence_id'] = pd.factorize(train_df['sentence_id'])[0]
dev_df['sentence_id'] = pd.factorize(dev_df['sentence_id'])[0]

# Define the labels
LABELS = json_dict["labels"]
print(LABELS)

print(train_df.shape, test_df.shape, dev_df.shape)
print(train_df.head())

```

Refer to [the demo](systems/dummy/dummy.py) to see an example.

# Contributing to the benchmark

Should you wish to contribute an entry, feel free to submit a folder like the [dummy](systems/dummy) with or without the code used. The results json file name should end with `.predictions.json` and the content should be structured like this:

```json
{
    "system": "Pick a name for your system",
    "predictions": [
        {   "train": "what you trained on", # e.g. data/hr500k.conllup_extracted.json-train
            "test": "what you evaluated on",# e.g. data/hr500k.conllup_extracted.json-test
            "predictions": [....] # The length of predictions should match the length of test data
        },
    ],
    # Additional information, e.g. fine-tuning params:
    "model": "EMBEDDIA/crosloengual-bert",
    "lr": "4e-5",
    "epoch": "15"
}
```
F1 micro and macro scores will be used to evaluate and compare systems.
