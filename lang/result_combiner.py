import json
import re
from functools import partial
from pathlib import Path

import pandas as pd
from sklearn.metrics import f1_score

macro = partial(f1_score,
                average="macro"
                )
micro = partial(f1_score,
                average="micro"
                )


mention_re = re.compile(r'@\S+')
hashtag_re = re.compile(r'#\S+')
url_re = re.compile(r'http\S+')
space_re = re.compile(r'\s+')


def clean_tweets(text):
    return space_re.sub(' ', url_re.sub(' ', hashtag_re.sub(' ', mention_re.sub(' ', text))).replace(' RT ', ' ').lower()).strip()


def load_twitter_dataset(categories=['bs', 'hr', 'sr', 'me']):
    twitter_dataset = json.load(open('data/Twitter-HBS.json'))
    X = {'train': [], 'dev': [], 'test': []}
    y = {'train': [], 'dev': [], 'test': []}
    for instance in twitter_dataset:
        lang = instance['language']
        split = instance['split']
        if lang in categories:
            y[split].append(lang)
            X[split].append(clean_tweets(' '.join(instance['tweets'])))
    return X, y


def load_setimes_dataset():
    setimes_dataset = json.load(open('data/SETimes.HBS.json'))
    X = {'train': [], 'dev': [], 'test': []}
    y = {'train': [], 'dev': [], 'test': []}
    for instance in setimes_dataset:
        lang = instance['language']
        split = instance['split']
        y[split].append(lang)
        X[split].append(instance['text'].lower())
    return X, y


twitter_X, twitter_y = load_twitter_dataset()
twitter3_X, twitter3_y = load_twitter_dataset(['bs', 'hr', 'sr'])
setimes_X, setimes_y = load_setimes_dataset()

p = Path(".")
found_directories = sorted([
    str(i) for i in p.iterdir()
    if i.is_dir() and not str(i).endswith("data")
])
found_predictions = [
    str(list(Path(i).glob("*.predictions.json"))[0]) for i in found_directories
]

entries = []
for pred in found_predictions:
    entry = Path(pred).read_text()
    entry = json.loads(entry)
    system = entry.get("system")
    entrydf = pd.DataFrame(entry["predictions"])
    mapper = {
        "setimes": setimes_y["test"],
        "twitter3": twitter3_y["test"],
        "twitter": twitter_y["test"]
    }
    entrydf["y_true"] = [mapper.get(i) for i in entrydf.test]
    entrydf["macroF1"] = [macro(y_true=y_true, y_pred=y_pred)
                          for y_true, y_pred in zip(entrydf.y_true, entrydf.predictions)]
    entrydf["microF1"] = [micro(y_true=y_true, y_pred=y_pred)
                          for y_true, y_pred in zip(entrydf.y_true, entrydf.predictions)]
    entrydf["system"] = system
    entries.append(entrydf)
df = pd.concat(entries, ignore_index=True)
df = df.loc[:, "system train test macroF1 microF1".split()]

resultsmd = "# Autogenerated comparison of results on different test sets:\n"
for test in df.test.unique():
    resultsmd += f"## Test data: {test}\n"
    subset = df[df.test == test].sort_values(
        by="macroF1", ascending=False).reset_index(drop=True)
    resultsmd += subset.to_markdown() + "\n"

readme = Path("README.md").read_text().split(
    "# Autogenerated comparison of results on different test sets:\n")[0] + resultsmd
Path("README.md").write_text(readme)