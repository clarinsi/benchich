| Model               | Test Dataset             |   Macro F1 |   Micro F1 |   Epochs |   Learning Rate |
|:--------------------|:-------------------------|-----------:|-----------:|---------:|----------------:|
| xlm-r-slobertic     | reldi-normtagner-hr.json |      0.817 |      0.983 |       11 |           4e-05 |
| xlm-r-bertic        | reldi-normtagner-hr.json |      0.799 |      0.983 |       11 |           4e-05 |
| csebert             | reldi-normtagner-hr.json |      0.789 |      0.981 |        7 |           4e-05 |
| bertic              | reldi-normtagner-hr.json |      0.787 |      0.981 |       10 |           4e-05 |
| xlm-r-large         | reldi-normtagner-hr.json |      0.779 |      0.982 |       11 |           4e-05 |
| xlm-r-base          | reldi-normtagner-hr.json |      0.744 |      0.979 |        8 |           4e-05 |
| dummy-stratified    | reldi-normtagner-hr.json |      0.099 |      0.846 |      nan |         nan     |
| dummy-most_frequent | reldi-normtagner-hr.json |      0.096 |      0.918 |      nan |         nan     |