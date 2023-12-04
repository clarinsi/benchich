# Named entity recognition benchmark for Croatian and Serbian

The purpose of this subrepo is gathering and comparison of results, obtained on named entity recognition (NER).

The benchmark consists of 4 datasets, manually-annotated with named entitites:
 - standard Croatian
 - non-standard Croatian
 - standard Serbian
 - non-standard Serbian

## Benchmark scores

Benchmark scores were calculated only once per system. Finetuning hyperparameters are listed in the json submission files, where applicable.

### Standard Croatian

The models are tested on the test split of [Croatian linguistic training corpus hr500k 2.0](http://hdl.handle.net/11356/1792).

| Model           | Test Dataset   |   Macro F1 |   Micro F1 |   Epochs |   Learning Rate |
|:----------------|:---------------|-----------:|-----------:|---------:|----------------:|
| [crosloengual-bert](https://huggingface.co/EMBEDDIA/crosloengual-bert)         | hr500k.json    |      0.627 |      0.959 |        4 |           4e-05 |
| [BERTić](https://huggingface.co/classla/bcms-bertic)          | hr500k.json    |      0.596 |      0.957 |        9 |           4e-05 |
| [XLM-R-base](https://huggingface.co/xlm-roberta-base)      | hr500k.json    |      0.568 |      0.955 |        5 |           4e-05 |
| [XLM-R-SloBERTić ](https://huggingface.co/classla/xlm-r-slobertic) | hr500k.json    |      0.158 |      0.922 |        7 |           4e-05 |
| [XLM-R-BERTić](https://huggingface.co/classla/xlm-r-bertic)    | hr500k.json    |      0.096 |      0.917 |        7 |           4e-05 |
| [XLM-R-large](https://huggingface.co/xlm-roberta-large)     | hr500k.json    |      0.096 |      0.917 |        7 |           4e-05 |

### Non-Standard Croatian

The models are tested on the test split of [Croatian Twitter training corpus ReLDI-NormTagNER-hr 3.0](http://hdl.handle.net/11356/1793).

| Model           | Test Dataset             |   Macro F1 |   Micro F1 |   Epochs |   Learning Rate |
|:----------------|:-------------------------|-----------:|-----------:|---------:|----------------:|
| [crosloengual-bert](https://huggingface.co/EMBEDDIA/crosloengual-bert)         | reldi-normtagner-hr.json |      0.517 |      0.956 |        7 |           4e-05 |
| [BERTić](https://huggingface.co/classla/bcms-bertic)          | reldi-normtagner-hr.json |      0.495 |      0.961 |       10 |           4e-05 |
| [XLM-R-base](https://huggingface.co/xlm-roberta-base)      | reldi-normtagner-hr.json |      0.404 |      0.956 |        8 |           4e-05 |
| [XLM-R-BERTić](https://huggingface.co/classla/xlm-r-bertic)    | reldi-normtagner-hr.json |      0.096 |      0.918 |       11 |           4e-05 |
| [XLM-R-large](https://huggingface.co/xlm-roberta-large)     | reldi-normtagner-hr.json |      0.096 |      0.918 |       11 |           4e-05 |
| [XLM-R-SloBERTić ](https://huggingface.co/classla/xlm-r-slobertic) | reldi-normtagner-hr.json |      0.096 |      0.918 |       11 |           4e-05 |

### Standard Serbian

The models are tested on the test split of [Serbian linguistic training corpus SETimes.SR 2.0](http://hdl.handle.net/11356/1843).

| Model           | Test Dataset     |   Macro F1 |   Micro F1 |   Epochs |   Learning Rate |
|:----------------|:-----------------|-----------:|-----------:|---------:|----------------:|
| [BERTić](https://huggingface.co/classla/bcms-bertic)          | set.sr.plus.json |      0.618 |      0.954 |       10 |           4e-05 |
| [crosloengual-bert](https://huggingface.co/EMBEDDIA/crosloengual-bert)         | set.sr.plus.json |      0.612 |      0.953 |        9 |           4e-05 |
| [XLM-R-base](https://huggingface.co/xlm-roberta-base)      | set.sr.plus.json |      0.604 |      0.953 |        6 |           4e-05 |
| [XLM-R-large](https://huggingface.co/xlm-roberta-large)     | set.sr.plus.json |      0.597 |      0.952 |       13 |           4e-05 |
| [XLM-R-BERTić](https://huggingface.co/classla/xlm-r-bertic)    | set.sr.plus.json |      0.59  |      0.953 |       13 |           4e-05 |
| [XLM-R-SloBERTić ](https://huggingface.co/classla/xlm-r-slobertic) | set.sr.plus.json |      0.094 |      0.881 |       13 |           4e-05 |

### Non-Standard Serbian

The models are tested on the test split of [Serbian Twitter training corpus ReLDI-NormTagNER-sr 3.0](http://hdl.handle.net/11356/1794).

| Model           | Test Dataset             |   Macro F1 |   Micro F1 |   Epochs |   Learning Rate |
|:----------------|:-------------------------|-----------:|-----------:|---------:|----------------:|
| [BERTić](https://huggingface.co/classla/bcms-bertic)          | reldi-normtagner-sr.json |      0.518 |      0.976 |       10 |           4e-05 |
| [crosloengual-bert](https://huggingface.co/EMBEDDIA/crosloengual-bert)         | reldi-normtagner-sr.json |      0.512 |      0.973 |        7 |           4e-05 |
| [XLM-R-BERTić](https://huggingface.co/classla/xlm-r-bertic)    | reldi-normtagner-sr.json |      0.512 |      0.975 |       11 |           4e-05 |
| [XLM-R-base](https://huggingface.co/xlm-roberta-base)      | reldi-normtagner-sr.json |      0.491 |      0.972 |        8 |           4e-05 |
| [XLM-R-large](https://huggingface.co/xlm-roberta-large)     | reldi-normtagner-sr.json |      0.165 |      0.963 |       11 |           4e-05 |
| [XLM-R-SloBERTić ](https://huggingface.co/classla/xlm-r-slobertic) | reldi-normtagner-sr.json |      0.097 |      0.949 |       11 |           4e-05 |

## Data

The datasets used for benchmarking are:
- [Croatian linguistic training corpus hr500k 2.0](http://hdl.handle.net/11356/1792)
- [Croatian Twitter training corpus ReLDI-NormTagNER-hr 3.0](http://hdl.handle.net/11356/1793)
- [Serbian linguistic training corpus SETimes.SR 2.0](http://hdl.handle.net/11356/1843)
- [Serbian Twitter training corpus ReLDI-NormTagNER-sr 3.0](http://hdl.handle.net/11356/1794)

The datasets are available in the `data/datasets` directory.

To prepare the datasets:
1. move to the `data` directory: `cd data`
2. download the data from the CLARIN.SI repository with the `download_data.sh` script. This downloads the Croatian and Serbian datasets in a new folder `datasets` inside the directory and converts them from CONLLUP format to JSON, containing only the relevant information for NER:
```bash download_dataset.sh "s_Croatian" "ns_Croatian" "s_Serbian" "ns_Serbian" > dataset_preparation.log```.

You can use all available datasets or define just a couple of them as the arguments (e.g., if you want to download only standard and non-standard Serbian: "s_Serbian" "ns_Serbian").

See the `data/dataset_preparation.log` for more details on the dataset sizes, label distribution, etc.

This prepares the following files:

```
data
├── datasets
    ├── hr500k.json
    ├── reldi-normtagner-hr.json
    ├── set.sr.plus.json
    ├── reldi-normtagner-sr.json
```

The datasets are JSON files - dictionaries which consist of the following keys:
 - "labels" (list of NE labels used in the dataset)
 - "train", "dev", "test" (dataset splits)

"train", "dev", "test" are also dictionaries, with the following keys:
 - "sentence_id" (original sentence id)
 - "id" (integer sentence id - to be used for classification with Simple Transformers library which does not accept strings as ids)
 - "words" (word forms as they appear in the sentence)
 - "labels" (NE labels)


**Dataset sizes**

Dataset sizes in number of instances (words):

| split     | hr500k (HR_s) | ReLDI-NormTagNER-hr (HR_ns) | set.sr.plus (SR_s) | ReLDI-NormTagNER-sr (SR_ns) |
|-----------|:-------------:|:---------------------------:|:---------------------------:|:------------------:|
| train     |  398,681             |     71,967                  |    74,259                   | 73,943             |
| test      |   51,190            |         8,952                    |       11,421                      |      9,122              |
| dev       |    49,764           |    8,936                         |      11,993                       |      92,06              |
| **Total** |   **499,635**            |      **89,855**                       |      **97,673**                       |      **92,271**              |


An example of how to use the prepared datasets with the simpletransformers library:

```python
import json
import pandas as pd

# Define the path to the dataset
dataset_path = "datasets/set.sr.plus.json"

# Load the json file
with open(dataset_path, "r") as file:
    json_dict = json.load(file)

# Open the train, eval and test dictionaries as DataFrames
train_df = pd.DataFrame(json_dict["train"])
test_df = pd.DataFrame(json_dict["test"])
dev_df = pd.DataFrame(json_dict["dev"])

# Use id instead of sentence_ids (ids should not be strings) and discard id column
for df in [train_df, test_df, dev_df]:
    df["sentence_id"] = df["id"]
    df = df.drop(columns=["id"])

# Define the labels
LABELS = json_dict["labels"]
print(LABELS)

print(train_df.shape, test_df.shape, dev_df.shape)
print(train_df.head())

```


## Contributing to the benchmark

Should you wish to contribute an entry, feel free to submit a folder in the [systems](systems) directory with or without the code used (see the submission examples in the directory).

The results JSON file name should end with `.predictions.json` and the content should be structured like this:

```python
{
    "system": "Pick a name for your system",
    "predictions": [
        {   "train": "what you trained on", # e.g. data/hr500k.json-train
            "test": "what you evaluated on",# e.g. data/hr500k.json-test
            "predictions": [....] # The length of predictions should match the length of test data
        },
    ],
    # Additional information, e.g. fine-tuning params:
    "model": "EMBEDDIA/crosloengual-bert",
    "lr": "4e-5",
    "epoch": "15"
}
```

All submission JSON files should be saved in a `submissions` directory inside the system directory. They will be evaluated against the datasets in the `data/datasets` directory.

It is highly encouraged that you also provide additional information about your system in a README file, and that you provide the code used for the classification with the system.

## Evaluation

Micro and Macro F1 scores will be used to evaluate and compare systems.

The submissions are evaluated using the following code with the absolute path to the submissions directory (e.g., ``/home/tajak/NER-recognition/benchich/ner/systems/hugging-face-models/submissions``) as the argument:
```python eval.py "submission-path" > systems/hugging-face-models/evaluation.log```
