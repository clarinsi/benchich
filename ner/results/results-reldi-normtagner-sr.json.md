| Model               | Test Dataset             |   Macro F1 |   Micro F1 |   Epochs |   Learning Rate |
|:--------------------|:-------------------------|-----------:|-----------:|---------:|----------------:|
| bertic              | reldi-normtagner-sr.json |      0.829 |      0.987 |       10 |           4e-05 |
| xlm-r-bertic        | reldi-normtagner-sr.json |      0.823 |      0.989 |       11 |           4e-05 |
| xlm-r-large         | reldi-normtagner-sr.json |      0.798 |      0.986 |       11 |           4e-05 |
| xlm-r-slobertic     | reldi-normtagner-sr.json |      0.796 |      0.988 |       11 |           4e-05 |
| xlm-r-base          | reldi-normtagner-sr.json |      0.782 |      0.986 |        8 |           4e-05 |
| csebert             | reldi-normtagner-sr.json |      0.695 |      0.984 |        7 |           4e-05 |
| dummy-stratified    | reldi-normtagner-sr.json |      0.099 |      0.898 |      nan |         nan     |
| dummy-most_frequent | reldi-normtagner-sr.json |      0.097 |      0.949 |      nan |         nan     |