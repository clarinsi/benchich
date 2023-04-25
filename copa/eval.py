import json
import sys
outputs=json.load(open(sys.argv[1]))
for output in outputs['predictions']:
    correct=0
    unknown=0
    for line,prediction in zip(open('data/'+output['test']),output['predictions']):
        entry=json.loads(line)
        if entry['label']==prediction:
            correct+=1
        if prediction is None:
            unknown+=1
    print(output['test'])
    print(correct/500)
    print(unknown/500)