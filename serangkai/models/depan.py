
from .rules import Awalan
from .rules import Terikat
from .rules import Preposisi
from ..preprocessing import Preprocess

class Depan:
    """

    """
    def __init__(self):
        self.rules = []
        self.preprocess = None

    def predict(self, words):

        words = self.preprocess.preprocess(words)
        words_len = len(words)

        flagidx = []
        for idx, kata in enumerate(words, start=1):
            prediction = True
            for rule in self.rules:
                if rule.__class__.__name__ == 'Preposisi':
                    if kata.startswith('di'):
                        if len(kata) > 2:
                            prediction = rule.predict(kata)
                            if not prediction:
                                flagidx.append((idx, kata))
                elif kata in rule.kamus:
                    kata_next = idx < words_len

                    if kata_next:
                        prediction = rule.predict(kata, words[idx]) # True or False
                    else:
                        prediction = kata_next

                    if not prediction:
                        flagidx.append((idx, kata))
                        continue
        return flagidx

    def fit(self, rules=[Terikat, Awalan, Preposisi]):
        for Rule in rules:
            rule = Rule()
            rule.fit()
            self.rules.append(rule)

        self.preprocess = Preprocess()
        self.preprocess.fit()
        