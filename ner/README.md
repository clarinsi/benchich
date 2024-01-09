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
| [XLM-R-SloBERTić ](https://huggingface.co/classla/xlm-r-slobertic) | hr500k.json    |      0.934 |      0.992 |        7 |           4e-05 |
| [BERTić](https://huggingface.co/classla/bcms-bertic)          | hr500k.json    |      0.925 |      0.991 |        9 |           4e-05 |
| [XLM-R-BERTić](https://huggingface.co/classla/xlm-r-bertic)    | hr500k.json    |      0.923 |      0.991 |        7 |           4e-05 |
| [crosloengual-bert](https://huggingface.co/EMBEDDIA/crosloengual-bert)         | hr500k.json    |      0.921 |      0.991 |        4 |           4e-05 |
| [XLM-R-large](https://huggingface.co/xlm-roberta-large)     | hr500k.json    |      0.921 |      0.991 |        7 |           4e-05 |
| [XLM-R-base](https://huggingface.co/xlm-roberta-base)      | hr500k.json    |      0.908 |      0.989 |        5 |           4e-05 |
| dummy-stratified    | hr500k.json    |      0.1   |      0.85  |      nan |         nan     |
| dummy-most_frequent | hr500k.json    |      0.096 |      0.917 |      nan |         nan     |

### Non-Standard Croatian

The models are tested on the test split of [Croatian Twitter training corpus ReLDI-NormTagNER-hr 3.0](http://hdl.handle.net/11356/1793).

| Model           | Test Dataset             |   Macro F1 |   Micro F1 |   Epochs |   Learning Rate |
|:----------------|:-------------------------|-----------:|-----------:|---------:|----------------:|
| [XLM-R-SloBERTić ](https://huggingface.co/classla/xlm-r-slobertic) | reldi-normtagner-hr.json |      0.817 |      0.983 |       11 |           4e-05 |
| [XLM-R-BERTić](https://huggingface.co/classla/xlm-r-bertic)    | reldi-normtagner-hr.json |      0.799 |      0.983 |       11 |           4e-05 |
| [crosloengual-bert](https://huggingface.co/EMBEDDIA/crosloengual-bert)         | reldi-normtagner-hr.json |      0.789 |      0.981 |        7 |           4e-05 |
| [BERTić](https://huggingface.co/classla/bcms-bertic)          | reldi-normtagner-hr.json |      0.787 |      0.981 |       10 |           4e-05 |
| [XLM-R-large](https://huggingface.co/xlm-roberta-large)     | reldi-normtagner-hr.json |      0.779 |      0.982 |       11 |           4e-05 |
| [XLM-R-base](https://huggingface.co/xlm-roberta-base)          | reldi-normtagner-hr.json |      0.76  |      0.978 |        8 |           4e-05 |
| dummy-stratified    | reldi-normtagner-hr.json |      0.099 |      0.846 |      nan |         nan     |
| dummy-most_frequent | reldi-normtagner-hr.json |      0.096 |      0.918 |      nan |         nan     |

### Standard Serbian

The models are tested on the test split of [Serbian linguistic training corpus SETimes.SR 2.0](http://hdl.handle.net/11356/1843).

| Model           | Test Dataset     |   Macro F1 |   Micro F1 |   Epochs |   Learning Rate |
|:----------------|:-----------------|-----------:|-----------:|---------:|----------------:|
| [XLM-R-SloBERTić ](https://huggingface.co/classla/xlm-r-slobertic) | set.sr.plus.json |      0.944 |      0.992 |       13 |           4e-05 |
| [XLM-R-large](https://huggingface.co/xlm-roberta-large)     | set.sr.plus.json |      0.936 |      0.991 |       13 |           4e-05 |
| [XLM-R-BERTić](https://huggingface.co/classla/xlm-r-bertic)    | set.sr.plus.json |      0.936 |      0.992 |       13 |           4e-05 |
| [crosloengual-bert](https://huggingface.co/EMBEDDIA/crosloengual-bert)         | set.sr.plus.json |      0.931 |      0.992 |        9 |           4e-05 |
| [BERTić](https://huggingface.co/classla/bcms-bertic)          | set.sr.plus.json |      0.93  |      0.991 |       10 |           4e-05 |
| [XLM-R-base](https://huggingface.co/xlm-roberta-base)      | set.sr.plus.json |      0.918 |      0.99  |        6 |           4e-05 |
| dummy-stratified    | set.sr.plus.json |      0.1   |      0.787 |      nan |         nan     |
| dummy-most_frequent | set.sr.plus.json |      0.094 |      0.881 |      nan |         nan     |



### Non-Standard Serbian

The models are tested on the test split of [Serbian Twitter training corpus ReLDI-NormTagNER-sr 3.0](http://hdl.handle.net/11356/1794).

| Model           | Test Dataset             |   Macro F1 |   Micro F1 |   Epochs |   Learning Rate |
|:----------------|:-------------------------|-----------:|-----------:|---------:|----------------:|
| [BERTić](https://huggingface.co/classla/bcms-bertic)          | reldi-normtagner-sr.json |      0.829 |      0.987 |       10 |           4e-05 |
| [XLM-R-BERTić](https://huggingface.co/classla/xlm-r-bertic)    | reldi-normtagner-sr.json |      0.823 |      0.989 |       11 |           4e-05 |
| [XLM-R-large](https://huggingface.co/xlm-roberta-large)     | reldi-normtagner-sr.json |      0.798 |      0.986 |       11 |           4e-05 |
| [XLM-R-SloBERTić ](https://huggingface.co/classla/xlm-r-slobertic) | reldi-normtagner-sr.json |      0.796 |      0.988 |       11 |           4e-05 |
| [XLM-R-base](https://huggingface.co/xlm-roberta-base)      | reldi-normtagner-sr.json |      0.782 |      0.986 |        8 |           4e-05 |
| [crosloengual-bert](https://huggingface.co/EMBEDDIA/crosloengual-bert)         | reldi-normtagner-sr.json |      0.695 |      0.984 |        7 |           4e-05 |
| dummy-stratified    | reldi-normtagner-sr.json |      0.099 |      0.898 |      nan |         nan     |
| dummy-most_frequent | reldi-normtagner-sr.json |      0.097 |      0.949 |      nan |         nan     |


## Data

The datasets used for benchmarking are:
- [Croatian linguistic training corpus hr500k 2.0](http://hdl.handle.net/11356/1792)
- [Croatian Twitter training corpus ReLDI-NormTagNER-hr 3.0](http://hdl.handle.net/11356/1793)
- [Serbian linguistic training corpus SETimes.SR 2.0](http://hdl.handle.net/11356/1843)
- [Serbian Twitter training corpus ReLDI-NormTagNER-sr 3.0](http://hdl.handle.net/11356/1794)

The datasets are available in the `data/datasets` directory.

If you would wish to prepare the datasets from scratch:
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
 - "sentence_id" (integer sentence id - to be used for classification with Simple Transformers library which does not accept strings as ids)
 - "words" (word forms as they appear in the sentence)
 - "labels" (NE labels)
 - "original_id" (original sentence id)


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

# Drop original_id
for df in [train_df, test_df, dev_df]:
    df.drop(columns=["original_id"], inplace=True)

# Define the labels
LABELS = json_dict["labels"]
print(LABELS)

print(train_df.shape, test_df.shape, dev_df.shape)
print(train_df.head())

```


## Contributing to the benchmark

Should you wish to contribute an entry, feel free to submit a folder in the [systems](systems) directory with or without the code used (see the submission examples in the directory).

The results JSON file name should start with `submission-` and the content should be structured like this:

```python
{
    "system": "Pick a name for your system",
    "predictions": [
        {   "train": "what you trained on", # e.g. "hr500k.json (train split)"
            "test": "what you evaluated on",# e.g. "hr500k.json (test split)"
            "predictions": [....] # The length of predictions should match the length of test data
        },
    ],
    # Additional information, e.g. fine-tuning params:
    "model": "EMBEDDIA/crosloengual-bert",
    "lr": "4e-5",
    "epoch": "15"
}
```

All submission JSON files should be saved in a `submissions` directory inside the directory for your system. They will be evaluated against the datasets in the `data/datasets` directory.

It is highly encouraged that you also provide additional information about your system in a README file, and that you provide the code used for the classification with the system.

## Evaluation

Micro and Macro F1 scores will be used to evaluate and compare systems.

The submissions are evaluated using the following code with the absolute path to the submissions directory (e.g., ``/home/tajak/NER-recognition/benchich/ner/systems/hugging-face-models/submissions``) as the argument. The log file is to be saved in the relevant system directory:
```python eval.py "submission-path" > systems/hugging-face-models/evaluation.log```
