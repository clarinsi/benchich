The gpt-4 model queried via the OpenAI API

The prompt is constructed in the following manner for causes (example in Macedonian):

```
Given the premise "Предметот беше спакуван во обвивка со меурчиња.", and that we are looking for the cause of this premise, which hypothesis seems more plausible?
Hypothesis 1: "Беше кршлив.".
Hypothesis 2: "Беше мал.".
Please answer only with "1" or "2".
```

In case of effects, the prompt is constructed as follows (again Macedonian
example):

```
Given the premise "Ги испразнив џебовите.", and that we are wondering what happened as a result of this premise, which hypothesis seems more plausible?
Hypothesis 1: "Најдов дел од карта.".
Hypothesis 2: "Најдов оружје.".
Please answer only with "1" or "2".
```

