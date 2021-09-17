import json
import joblib
from sklearn.pipeline import Pipeline
import pandas as pd

if __name__ == '__main__':
    with open('test.json', 'r', encoding='utf-8') as inf:
        data = json.load(inf)
    model: Pipeline = joblib.load('modelpipeline_ru.pkl')
    print(model.predict([input()])[0])
    '''
    res = {'text': [], 'type': []}
    print(len(data))
    test = data[:100]
    for record in test:
        res['text'].append(record['text'])
        res['type'].append(model.predict([record['text']])[0])
    df = pd.DataFrame(res)
    print(df.head(10))
    df.to_csv('test.csv')
    '''
