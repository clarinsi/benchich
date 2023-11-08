# Sentiment identification

The purpose of this subrepo is gathering and comparison of results, obtained on sentiment regression.

## Data

The dataset used for benchmarking is [ParlaSent](https://arxiv.org/abs/2309.09783). It is available on [Clarin.si reposizory](https://www.clarin.si/repository/xmlui/handle/11356/1868) as well as on [HuggingFace dataset hub](https://huggingface.co/datasets/classla/ParlaSent). 

For the purpose of this task we cast the ordinal labels into integers with the following mapping:

```json
{
    "Negative": 0.0,
    "M_Negative": 1.0,
    "N_Neutral": 2.0,
    "P_Neutral": 3.0,
    "M_Positive": 4.0,
    "Positive": 5.0,
}
```

The data can be prepared by running [the prepared script](data/dataloader.py) when in the `data` directory. This will download the following files:

```
data
├── ParlaSent_BCS.jsonl
├── ParlaSent_BCS_test.jsonl
├── ParlaSent_CZ.jsonl
├── ParlaSent_EN.jsonl
├── ParlaSent_EN_test.jsonl
├── ParlaSent_SK.jsonl
└── ParlaSent_SL.jsonl
```

Each of the files contains 2600 instances. The files with `test.jsonl` are used as an independent test set, all others are internally already split in train, dev, and test splits.

At this point we are most interested in the performance of BCS languages: `ParlaSent_BCS_test.jsonl` is used for testing and should not be trained on.

## Systems and results

Should you wish to contribute an entry, feel free to submit a folder like the [dummy](systems/dummy) with or without the code used. The results json file name should end with `.predictions.json` and the content should be structured like this:

```json
{
    "system": "Pick a name for your system",
    "predictions": [
        {   "train": "what did you train on", # e.g. data/ParlaSent_BCS.jsonl
            "test": "what you evaluated on",# e.g. data/ParlaSent_BCS_test.jsonl
            "predictions": [....] # The length of predictions should match the lentgh of test data
        },
        {   "train": "data/ParlaSent_BCS.jsonl/train_split",
            "test": "data/ParlaSent_BCS.jsonl/dev_split",
            "predictions": [....]
        },
    ]

}
```
r^2 metric is used to rank different systems.
# Currently available systems

| system                                                                 | train               | test                     |   r^2 |
|:-----------------------------------------------------------------------|:--------------------|:-------------------------|------:|
| dummy (mean)                                                           | ParlaSent_BCS.jsonl | ParlaSent_BCS_test.jsonl | -0.12 |
| XLM-Roberta-Base                                                       | ParlaSent_BCS.jsonl | ParlaSent_BCS_test.jsonl | 0.500 |
| [crosloengual-bert](https://huggingface.co/EMBEDDIA/crosloengual-bert) | ParlaSent_BCS.jsonl | ParlaSent_BCS_test.jsonl | 0.537 |
| XLM-Roberta-Large                                                      | ParlaSent_BCS.jsonl | ParlaSent_BCS_test.jsonl | 0.605 |
| [BERTić](https://huggingface.co/classla/bcms-bertic)                   | ParlaSent_BCS.jsonl | ParlaSent_BCS_test.jsonl | 0.612 |
| [xlm-r-parlasent](https://huggingface.co/classla/xlm-r-parlasent)      | ParlaSent_BCS.jsonl | ParlaSent_BCS_test.jsonl | 0.615 |
