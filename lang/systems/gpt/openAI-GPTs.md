# OpenAI's GPT models

We evaluate the following models:
- GPT-4o ("gpt-4o-2024-08-06"),
- GPT-4o-mini ("gpt-4o-mini-2024-07-18")

We use the following prompt:
```python

labels_dict = {"Croatian": 1, "Serbian": 2, "Montenegrin": 3, "Bosnian": 4}

			messages= [
			{
				"role": "user",
				"content": f"""
				### Task
				Your task is to determine which South Slavic language is used in the provided text: Croatian, Serbian, Montenegrin, or Bosnian. Your choice should be based on the linguistic differences (e.g., the use of ijekavian vs. ekavian dialects), vocabulary choices (e.g., hljeb vs. kruh) and any specific local or national references. If multiple language labels are plausible, choose the most likely one based on the text content. Always provide a language label, even if you are not sure.

				### Output format
					Return a valid JSON dictionary with the following key: 'lang' and a value should be an integer which represents one of the labels according to the following dictionary: {labels_dict}.

					
					Text: '{text}'
			"""
				}
```
