# COPA - Choice of Plausible Alternatives

Datasets in this benchmark are the following:
- The COPA part of the Slovenian SuperGLUE translation (http://hdl.handle.net/11356/1380)
- The COPA-HR dataset (http://hdl.handle.net/11356/1404)
- The COPA-SR dataset (https://www.clarin.si/info/k-centre/)
- The COPA-MK dataset (http://hdl.handle.net/11356/1687)

| model | COPA-SL | COPA-HR | COPA-SR | COPA-SR-LAT | COPA-MK |
|-|-|-|-|-|-|
| gpt-3.5-turbo | 83.4 | 85.4 | 79.4 | 83.6 | 76.2 |


Given that some part of the error of models is due to their uncertainty,
below we are giving the percentage of instances for which we did not receive
a classification response.

| model | COPA-SL | COPA-HR | COPA-SR | COPA-SR-LAT | COPA-MK |
|-|-|-|-|-|-|
| gpt-3.5-turbo | 5.4 | 5.2 | 6.8 | 6.6 | 5.4 |
