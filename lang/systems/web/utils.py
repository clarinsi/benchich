import os
import parse
import logging
import pandas as pd
from typing import Set, List, Tuple
from transliterate import translit
chars_to_remove = {
    '!',
    '"',
    '#',
    '%',
    '&',
    "'",
    '(',
    ')',
    '*',
    '+',
    ',',
    '-',
    '.',
    '/',
    ':',
    ';',
    '<',
    '=',
    '>',
    '?',
    '[',
    ']',
    '_',
    '`',
    '«',
    '°',
    '²',
    '³',
    'µ',
    '·',
    '»',
    '½',
    '‑',
    '–',
    '‘',
    '’',
    '“',
    '”',
    '„',
    '•',
    '…',
    '‰',
    '″',
    '₂',
    '₃',
    '€',
    '™',
    '→',
    '−',
    '∕',
    '😀',
    '😉',
    '🙁',
    '🙂'

}

import json

import re
mention_re=re.compile(r'@\S+')
hashtag_re=re.compile(r'#\S+')
url_re=re.compile(r'http\S+')
space_re=re.compile(r'\s+')

def clean_tweets(text):
    return space_re.sub(' ',url_re.sub(' ',hashtag_re.sub(' ',mention_re.sub(' ',text))).replace(' RT ',' ').lower()).strip()

def load_twitter_dataset(categories=['bs','hr','sr','me']):
    twitter_dataset=json.load(open('../data/Twitter-HBS.json'))
    X={'train':[],'dev':[],'test':[]}
    y={'train':[],'dev':[],'test':[]}
    for instance in twitter_dataset:
        lang=instance['language']
        split=instance['split']
        if lang in categories:
            y[split].append(lang)
            X[split].append(clean_tweets(' '.join(instance['tweets'])))
    return X,y

def load_setimes_dataset():
    setimes_dataset=json.load(open('../data/SETimes.HBS.json'))
    X={'train':[],'dev':[],'test':[]}
    y={'train':[],'dev':[],'test':[]}
    for instance in setimes_dataset:
        lang=instance['language']
        split=instance['split']
        y[split].append(lang)
        X[split].append(instance['text'].lower())
    return X,y
        
        
LABELS = ["hr", "bs", "sr", "me"]
raw_dir = "/home/peterr/macocu/taskB/data/raw"
interim_dir = "/home/peterr/macocu/taskB/data/interim"
final_dir = "/home/peterr/macocu/taskB/data/final"


def remove_chars(input_text: str, chars_to_remove: Set[str] = chars_to_remove) -> Set[str]:
    for c in chars_to_remove:
        input_text = input_text.replace(c, "")
    return input_text


def transliterate(input_text: str) -> str:
    from transliterate import translit
    return translit(input_text, "sr", reversed=True)


def is_alpha(token: str) -> bool:
    import re
    pattern = "^[a-zšđčćž]+$"
    compiled_pattern = re.compile(pattern)
    return bool(compiled_pattern.match(token))


def get_N_tokens(N=5000, path="/home/peterr/macocu/task22/tokens.csv") -> set:
    """Loads tokens from CSV and returns as set of N most important for every language.

    Args:
        N (int, optional): Number of token per language to include. Defaults to 5000.
        path (str, optional): CSV file with token numbers per language. 
            Has columns (token,bswac_head_pp,cnrwac_head_pp,hrwac_head_pp,srwac_head_pp).
            Defaults to "/home/peterr/macocu/taskB/task4/toy_tokens.csv".

    Returns:
        set: set of most important N tokens for every language combination.
    """
    import pandas as pd
    import numpy as np
    df = pd.read_csv(path, index_col=0)

    df = df.iloc[~df.index.isna(), :]

    def filter_token(token: str) -> bool:
        token = token.replace(" ", "")
        if len(token) < 3:
            return False
        return any([vowel in token for vowel in "aeiou"])
    df["keep"] = df.index.copy()
    df["keep"] = df.keep.apply(filter_token)
    df = df.loc[df.keep, :]
    df.drop(columns=["keep"], inplace=True)
    NUM_FEATS = N
    for column in df.columns:
        new_column_name = column + "_f"
        corpus_size = df[column].sum()
        df[new_column_name] = df[column] * 1e6 / corpus_size

    N = 1

    df["HR_SR"] = (df["hrwac_head_pp_f"] + N) / (df["srwac_head_pp_f"] + N)
    df["SR_HR"] = (df["srwac_head_pp_f"] + N) / (df["hrwac_head_pp_f"] + N)

    df["HR_CNR"] = (df["hrwac_head_pp_f"] + N) / (df["cnrwac_head_pp_f"] + N)
    df["CNR_HR"] = (df["cnrwac_head_pp_f"] + N) / (df["hrwac_head_pp_f"] + N)

    df["HR_BS"] = (df["hrwac_head_pp_f"] + N) / (df["bswac_head_pp_f"] + N)
    df["BS_HR"] = (df["bswac_head_pp_f"] + N) / (df["hrwac_head_pp_f"] + N)

    df["BS_SR"] = (df["bswac_head_pp_f"] + N) / (df["srwac_head_pp_f"] + N)
    df["SR_BS"] = (df["srwac_head_pp_f"] + N) / (df["bswac_head_pp_f"] + N)

    df["BS_CNR"] = (df["bswac_head_pp_f"] + N) / (df["cnrwac_head_pp_f"] + N)
    df["CNR_BS"] = (df["cnrwac_head_pp_f"] + N) / (df["bswac_head_pp_f"] + N)

    df["CNR_SR"] = (df["cnrwac_head_pp_f"] + N) / (df["srwac_head_pp_f"] + N)
    df["SR_CNR"] = (df["srwac_head_pp_f"] + N) / (df["cnrwac_head_pp_f"] + N)

    combos = ['HR_SR', 'SR_HR', 'HR_CNR', 'CNR_HR', 'HR_BS', 'BS_HR',
              'BS_SR', 'SR_BS', 'BS_CNR', 'CNR_BS', 'CNR_SR', 'SR_CNR']
    important_features = set()
    for lang_comb in combos:
        s = df[lang_comb].sort_values(ascending=False)
        current_features = s.index[:NUM_FEATS].values
        important_features = important_features.union(set(current_features))
    try:
        important_features.remove(np.nan)
    except KeyError:
        pass
    return important_features


def read_and_split_file(path: str) -> List[str]:
    """Reads a text file and returns a list of strings. Every string is a document.
    Expects the input to be corpus where documents are separated with empty lines.
    Returns only the words that are lowercase alpha.

    Args:
        path (str): path of the text file to read.

    Returns:
        List[str]: list of filtered documents.
    """
    texts = list()
    chunk = ""
    with open(path, "r") as f:
        content = f.readlines()
    for line in content:
        # Handle splits
        if line == "\n":
            texts.append(chunk)
            chunk = ""
        # Filter only lowercase alphabetical words:
        from utils import is_alpha
        line = line.replace("\n", " ")
        # words = [w if is_alpha(w) else " " for w in line.split(" ")]
        words = [w for w in line.split(" ")]
        chunk += " ".join(words)
    return texts


def load_fasttext(path) -> Tuple[List[str], List[str]]:
    SETimes = list()
    with open(path, "r") as f:
        lines = f.readlines()
        SETimes.extend(lines)

    p = parse.compile("__label__{lang} {text}")
    langs = list()
    texts = list()

    for line in SETimes:
        results = p.parse(line)
        if not results:
            logging.error(f"Error parsing line {line}")
            continue
        langs.append(results["lang"])
        texts.append(results["text"])

    eval_df = pd.DataFrame(data={"text": texts, "labels": langs})
    return eval_df


from tqdm import tqdm
from pathlib import Path
from utils import *
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import CountVectorizer
import pickle



def get_stats(
    train_df: pd.DataFrame,
    eval_df: pd.DataFrame,
    classifier_type: str = "LinearSVC",
    vectorizer_type: str = "ngram",
    N: int = 100,
    random_state: int = 42,
    charN: int = 3,
    binary: bool = True,
) -> dict:

    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import LinearSVC
    from sklearn.feature_extraction.text import CountVectorizer
    LABELS = ["hr", "bs", "sr", "me"] if "me" in eval_df.labels else ["hr", "bs", "sr"]
    
    train_labels = train_df.labels.tolist()
    eval_labels = eval_df.labels.tolist()
    train_text = train_df.text.tolist()
    eval_text = eval_df.text.tolist()
    
    if classifier_type == "LinearSVC":
        clf = LinearSVC(dual=False, random_state=random_state)
    elif classifier_type == "NaiveBayes":
        clf = GaussianNB()
    else:
        raise AttributeError(f"Got {classifier_type=}, can only be LinearSVC or NaiveBayes")
    
    
    if vectorizer_type == "web":
        vec = CountVectorizer(
            vocabulary=get_N_tokens(N), lowercase=True, binary=binary)
    elif vectorizer_type == "ngram":
        vec = CountVectorizer(analyzer="char", ngram_range=(3, charN))
    else:
        raise AttributeError(f"Got {vectorizer_type=}, can only be web or ngram")
    def evaluate(vec, clf, eval_df):
        eval_text = eval_df.text.tolist()
        train_vectors = vec.fit_transform(train_text) 
        eval_vectors = vec.transform(eval_text)
        clf.fit(train_vectors.toarray(), train_labels)
        y_pred = clf.predict(eval_vectors.toarray()).tolist()
        y_true = eval_df.labels.values.tolist()
        from sklearn.metrics import f1_score, ConfusionMatrixDisplay, confusion_matrix, accuracy_score

        macro = f1_score(y_true, y_pred, labels=LABELS, average="macro")
        micro = f1_score(y_true, y_pred, labels=LABELS,  average="micro")
        acc = accuracy_score(y_true, y_pred)
        cm = confusion_matrix(y_true, y_pred, labels=LABELS)
        return {
            "microF1": micro,
            "macroF1": macro,
            "y_true": y_true,
            "y_pred": y_pred
        }
    return evaluate(vec, clf, eval_df), vec, clf