import joblib
from nltk.util import pr
from sklearn.pipeline import Pipeline
from tokenizer import tokenize_sentence_ru

# tokeniozer.py required


class SentenceAnalizer:
    def __init__(self, model_file) -> None:
        self.model: Pipeline = joblib.load(model_file)

    def predict(self, sentence: str):
        return self.model.predict([sentence])[0]

    def predict_proba(self, sentence: str):
        return self.model.predict_proba([sentence])


if __name__ == '__main__':
    s = SentenceAnalizer('modelpipeline.joblib')
    print(s.predict('You are a terrible fool'))
    print(s.predict_proba('Nice move'))
