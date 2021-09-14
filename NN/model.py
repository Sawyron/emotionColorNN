import joblib
from nltk.util import pr
from sklearn.pipeline import Pipeline

# tokeniozer.py required
class SentenceAnalizer:
    def __init__(self, model_file) -> None:
        self.model: Pipeline = joblib.load(model_file)

    def predict(self, sentence):
        return self.model.predict([sentence])


if __name__ == '__main__':
    s = SentenceAnalizer('modelpipeline.joblib')
    print(s.predict('Nice move'))
