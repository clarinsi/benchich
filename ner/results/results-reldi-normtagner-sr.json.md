| Model               | Test Dataset             |   Macro F1 |   Micro F1 |   Epochs |   Learning Rate |
|:--------------------|:-------------------------|-----------:|-----------:|---------:|----------------:|
| xlm-r-bertic        | reldi-normtagner-sr.json |      0.823 |      0.989 |       11 |           4e-05 |
| xlm-r-slobertic     | reldi-normtagner-sr.json |      0.803 |      0.987 |       11 |           4e-05 |
| bertic              | reldi-normtagner-sr.json |      0.793 |      0.987 |       10 |           4e-05 |
| xlm-r-large         | reldi-normtagner-sr.json |      0.788 |      0.986 |       11 |           4e-05 |
| xlm-r-base          | reldi-normtagner-sr.json |      0.724 |      0.985 |        8 |           4e-05 |
| csebert             | reldi-normtagner-sr.json |      0.72  |      0.986 |        7 |           4e-05 |
| dummy-stratified    | reldi-normtagner-sr.json |      0.099 |      0.898 |      nan |         nan     |
| dummy-most_frequent | reldi-normtagner-sr.json |      0.097 |      0.949 |      nan |         nan     |