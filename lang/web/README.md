# web

This method uses exterior web crawl data (not included in this repo) to extract most significant words for every language pair from a part of web data and then trains a Naive Bayes model on the rest of the data with a tokenizer, whose vocabulary consists only of top 100 most important words per language pair.

Words' _importance_ was calculated with a keyness score, which is in essence a smoothened ratio of a words frequency in one language and its frequency in the other language.

This was done for every of the 12 pairs (Croatian-Bosnian, Bosnian-Croatian, ...) and then concatenated.

The [script](web.py) runs this training pipeline and evaluates it on Twitter, SETimes, and Twitter3 data (the latter being a subset of Twitter dataset where only Croatian, Serbian, and Bosnian labels are present.)

It was found that compared with the [baseline model](../char_ngram_baseline/README.md) the results are not as good in-domain, but this method seems to be more robust when comparing models, trained on Twitter and evaluated on news articles or vice versa.


## New additions:

* A new joblib file was added, allowing for quick evaluation:
```python
import joblib
f = joblib.load("../lang/web/classify.joblib")
f("U njegovoj pratnji su ministarka turizma Fani Pali-Petralija, zamenik ministra ekonomije Petros Dukas i zamenik ministra inostranih poslova Teodoros Kasimis.")
# -> 'sr'
```