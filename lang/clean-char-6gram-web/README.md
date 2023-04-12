# clean-char-6gram-web

This method exploits MaCoCu web data for training a character 6-gram SGD classifier
from the scikit-learn package. For its training it selects 80 thousand sequences
per language. Each sequence is supposed to consist of letters and spaces
only, and be more than 100 characters long. As the gold label we use the
national top-level-domain information the text was published on, .ba for
Bosnian, .hr for Croatian, .me for Montenegrin and .rs for Serbian. We
transliterate all text into the Latin script.

We prepare the classifier in two flavours, for three languages (bs, hr, sr)
and four languages (bs, hr, me, sr), so that we can evaluate it on all three
evaluation datasets.

The results show stellar performance on the Twitter dataset, and acceptable
performance on the SETimes dataset. Our hypothesis is that our training data
clean-up (taking only sequences of letters and spaces) performed a feature
selection that seems to be very much needed on the Twitter dataset. We argue
that other approaches might be as efficient on the Twitter dataset if they
took up a heavier data clean-up.

The classification reports on each of the three evaluation datasets are listed
below:

```
setimes
              precision    recall  f1-score   support

          bs       0.69      0.99      0.81       312
          hr       0.99      0.57      0.72       313
          sr       1.00      0.99      0.99       296

    accuracy                           0.85       921
   macro avg       0.89      0.85      0.84       921
weighted avg       0.89      0.85      0.84       921

twitter3
              precision    recall  f1-score   support

          bs       1.00      0.93      0.97        15
          hr       1.00      1.00      1.00        18
          sr       0.99      1.00      0.99        79

    accuracy                           0.99       112
   macro avg       1.00      0.98      0.99       112
weighted avg       0.99      0.99      0.99       112

twitter4
              precision    recall  f1-score   support

          bs       0.64      0.93      0.76        15
          hr       1.00      1.00      1.00        18
          me       1.00      0.09      0.17        11
          sr       0.96      1.00      0.98        79

    accuracy                           0.91       123
   macro avg       0.90      0.76      0.73       123
weighted avg       0.93      0.91      0.88       123
```

The problem with not-stellar performance on setimes seems to be that the classifier often confuses Croatian documents to be Bosnian. A feature-based analysis would be needed to identify why this is the case.

For now this classifier has been used on all non-national-top-level domains in the HBS MaCoCu data to split those up into one of the four languages.
