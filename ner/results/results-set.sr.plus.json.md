| Model               | Test Dataset     |   Macro F1 |   Micro F1 |   Epochs |   Learning Rate |
|:--------------------|:-----------------|-----------:|-----------:|---------:|----------------:|
| xlm-r-slobertic     | set.sr.plus.json |      0.944 |      0.992 |       13 |           4e-05 |
| xlm-r-large         | set.sr.plus.json |      0.936 |      0.991 |       13 |           4e-05 |
| xlm-r-bertic        | set.sr.plus.json |      0.936 |      0.992 |       13 |           4e-05 |
| csebert             | set.sr.plus.json |      0.931 |      0.992 |        9 |           4e-05 |
| bertic              | set.sr.plus.json |      0.93  |      0.991 |       10 |           4e-05 |
| xlm-r-base          | set.sr.plus.json |      0.918 |      0.99  |        6 |           4e-05 |
| dummy-stratified    | set.sr.plus.json |      0.1   |      0.787 |      nan |         nan     |
| dummy-most_frequent | set.sr.plus.json |      0.094 |      0.881 |      nan |         nan     |