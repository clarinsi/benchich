# BENCHić-lang - the language discrimination part of the BENCHić benchmark

The task in this part of the benchmark is to be able to discriminate between the four languages this benchmark covers - Bosnian, Croatian, Serbian and Montenegrin.

The benchmark consists of two datasets - a newspaper-based one covering Bosnian, Croatian and Serbian, and another Twitter-based one, covering all four languages.

## `char_ngram_baseline`

This part covers the in- and cross-domain baselines, performed with character-3-gram tokenizer and a SVM classifier. Running
```python
python char_ngram_baseline.py 
```
performs the baseline experiments, outputs classification reports of different settings to stdout and saves predictions to `char_ngram_baseline.predictions.json`.

## `web`

This part covers the classifier, trained on web data: first the vocabulary gets extracted from web data, only 100 most significant words per language pair are propagated to the CountVectorizer tokenizer. This tokenizer and a different part of web data are then trained together and evaluated on Twitter and SETimes data. Run
```python
python web.py
```
performs the training and evaluation on SETimes, Twitter 3 (hr, bs, sr) and Twitter 4 (hr, bs, sr, me) data. The classification reports are output to stdout and predictions are saved in a json file in baseline-compatible format. 

Note that the web data is not included in this repository.

## `data`

This directory contains the data to be used for training and evaluation of the classifiers.

### SETimes
News articles in hr, bs, and sr.
### Twitter
Twitter data in hr, bs, sr, and me.
