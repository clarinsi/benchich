| Model               | Test Dataset             |   Macro F1 |   Micro F1 |   Epochs |   Learning Rate |
|:--------------------|:-------------------------|-----------:|-----------:|---------:|----------------:|
| csebert             | reldi-normtagner-hr.json |      0.517 |      0.956 |        7 |           4e-05 |
| bertic              | reldi-normtagner-hr.json |      0.495 |      0.961 |       10 |           4e-05 |
| xlm-r-base          | reldi-normtagner-hr.json |      0.404 |      0.956 |        8 |           4e-05 |
| Dummy               | reldi-normtagner-hr.json |      0.098 |      0.844 |      nan |         nan     |
| xlm-r-bertic        | reldi-normtagner-hr.json |      0.096 |      0.918 |       11 |           4e-05 |
| xlm-r-large         | reldi-normtagner-hr.json |      0.096 |      0.918 |       11 |           4e-05 |
| xlm-r-slobertic     | reldi-normtagner-hr.json |      0.096 |      0.918 |       11 |           4e-05 |
| Logistic Regression | reldi-normtagner-hr.json |      0.096 |      0.918 |      nan |         nan     |
| Naive Bayes         | reldi-normtagner-hr.json |      0.032 |      0.169 |      nan |         nan     |