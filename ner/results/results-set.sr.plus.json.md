| Model               | Test Dataset     |   Macro F1 |   Micro F1 |   Epochs |   Learning Rate |
|:--------------------|:-----------------|-----------:|-----------:|---------:|----------------:|
| bertic              | set.sr.plus.json |      0.618 |      0.954 |       10 |           4e-05 |
| csebert             | set.sr.plus.json |      0.612 |      0.953 |        9 |           4e-05 |
| xlm-r-base          | set.sr.plus.json |      0.604 |      0.953 |        6 |           4e-05 |
| xlm-r-large         | set.sr.plus.json |      0.597 |      0.952 |       13 |           4e-05 |
| xlm-r-bertic        | set.sr.plus.json |      0.59  |      0.953 |       13 |           4e-05 |
| Dummy               | set.sr.plus.json |      0.1   |      0.782 |      nan |         nan     |
| xlm-r-slobertic     | set.sr.plus.json |      0.094 |      0.881 |       13 |           4e-05 |
| Logistic Regression | set.sr.plus.json |      0.094 |      0.881 |      nan |         nan     |
| Naive Bayes         | set.sr.plus.json |      0.049 |      0.23  |      nan |         nan     |