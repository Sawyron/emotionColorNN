import json
import pandas as pd


def main():
    with open('train.json', 'r', encoding='utf-8') as inf:
        data = json.load(inf)
    df = pd.DataFrame(data)
    print(df.dtypes)
    df.pop('id')
    df.rename(columns={'text': 'comment', 'sentiment': 'type'}, inplace=True)
    df['type'] = df['type'].apply(
        lambda x: 0.0 if x == 'negative' else 1.0)
    df['comment'] = df['comment'].apply(str)
    df['type'] = df['type'].apply(float)
    df.to_csv('dataset_train_ru.csv')
    print(df.head(6))
    print(df.dtypes)


if __name__ == '__main__':
    main()
