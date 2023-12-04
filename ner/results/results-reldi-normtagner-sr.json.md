| Model               | Test Dataset             |   Macro F1 |   Micro F1 |   Epochs |   Learning Rate |
|:--------------------|:-------------------------|-----------:|-----------:|---------:|----------------:|
| bertic              | reldi-normtagner-sr.json |      0.518 |      0.976 |       10 |           4e-05 |
| csebert             | reldi-normtagner-sr.json |      0.512 |      0.973 |        7 |           4e-05 |
| xlm-r-bertic        | reldi-normtagner-sr.json |      0.512 |      0.975 |       11 |           4e-05 |
| xlm-r-base          | reldi-normtagner-sr.json |      0.491 |      0.972 |        8 |           4e-05 |
| xlm-r-large         | reldi-normtagner-sr.json |      0.165 |      0.963 |       11 |           4e-05 |
| Dummy               | reldi-normtagner-sr.json |      0.1   |      0.899 |      nan |         nan     |
| xlm-r-slobertic     | reldi-normtagner-sr.json |      0.097 |      0.949 |       11 |           4e-05 |
| Logistic Regression | reldi-normtagner-sr.json |      0.097 |      0.949 |      nan |         nan     |
| Naive Bayes         | reldi-normtagner-sr.json |      0.036 |      0.316 |      nan |         nan     |