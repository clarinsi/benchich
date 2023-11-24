# Sentiment identification benchmark

The purpose of this subrepo is gathering and comparison of results, obtained on sentiment regression.

# Benchmark scores

| system                                                                 | train               | test                     |   r^2 |
|:-----------------------------------------------------------------------|:--------------------|:-------------------------|------:|
| [BERTić](https://huggingface.co/classla/bcms-bertic)                   | ParlaSent_BCS.jsonl | ParlaSent_BCS_test.jsonl | 0.611 |
| [xlm-r-parlasent](https://huggingface.co/classla/xlm-r-parlasent)      | ParlaSent_BCS.jsonl | ParlaSent_BCS_test.jsonl | 0.601 |
| [XLM-R-SloBERTić ](https://huggingface.co/classla/xlm-r-slobertic)     | ParlaSent_BCS.jsonl | ParlaSent_BCS_test.jsonl | 0.578 |
| [XLM-R-BERTić](https://huggingface.co/classla/xlm-r-bertic)            | ParlaSent_BCS.jsonl | ParlaSent_BCS_test.jsonl | 0.576 |
| XLM-Roberta-Large                                                      | ParlaSent_BCS.jsonl | ParlaSent_BCS_test.jsonl | 0.547 |
| [crosloengual-bert](https://huggingface.co/EMBEDDIA/crosloengual-bert) | ParlaSent_BCS.jsonl | ParlaSent_BCS_test.jsonl | 0.547 |
| XLM-Roberta-Base                                                       | ParlaSent_BCS.jsonl | ParlaSent_BCS_test.jsonl | 0.402 |
| dummy (mean)                                                           | ParlaSent_BCS.jsonl | ParlaSent_BCS_test.jsonl |     0 |

# Data

The dataset used for benchmarking is [ParlaSent](https://arxiv.org/abs/2309.09783). It is available on [Clarin.si repository](https://www.clarin.si/repository/xmlui/handle/11356/1868) as well as on [HuggingFace dataset hub](https://huggingface.co/datasets/classla/ParlaSent). 

The data can be prepared by running [the prepared script](data/dataloader.py) from the `data` directory. This will download the following files:

```
data
├── ParlaSent_BCS.jsonl
└── ParlaSent_BCS_test.jsonl
```

Each of the files contains 2600 instances. The files ending with `test.jsonl` are used as an independent test set, all others are internally already split in train, dev, and test splits.

To use this data, `reconciliation` column should be used where present, and `annotator1` should be used elsewhere. The ordinal labels should be mapped with the following mapping to 
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

Refer to [the demo](systems/dummy/dummy.py) to see an example.

# Contributing to the benchmark

Should you wish to contribute an entry, feel free to submit a folder like the [dummy](systems/dummy) with or without the code used. The results json file name should end with `.predictions.json` and the content should be structured like this:

```json
{
    "system": "Pick a name for your system",
    "predictions": [
        {   "train": "what did you train on", # e.g. data/ParlaSent_BCS.jsonl
            "test": "what you evaluated on",# e.g. data/ParlaSent_BCS_test.jsonl
            "predictions": [....] # The length of predictions should match the lenght of test data
        },
    ]

}
```
r^2 metric will be used to evaluate and compare systems.
