import os
import pandas as pd


def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def fillCommentDict(table, directory, value):
    files = os.scandir(directory)
    for file in files:
        abs_file_name = os.path.join(directory, file.name)
        with open(abs_file_name, 'r', encoding='utf-8') as inf:
            data = inf.read()
            data = remove_html_tags(data)
            table['comment'].append(data)
            table['type'].append(value)


def readComments(directory: str):
    res = {'comment': [], 'type': []}
    fillCommentDict(res, directory + '\\pos', 1.0)
    fillCommentDict(res, directory + '\\neg', 0.0)
    return res


if __name__ == '__main__':
    test_dir = 'test'
    train_dir = 'train'
    data_table = readComments(train_dir)
    df = pd.DataFrame(data_table)
    df.to_csv('dataset_train_english.csv')
    data_table = readComments(test_dir)
    df = pd.DataFrame(data_table)
    df.to_csv('dataset_test_english.csv')
