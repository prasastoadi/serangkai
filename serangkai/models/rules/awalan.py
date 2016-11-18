from ...kamus import load_kamus

class Awalan:

    def __init__(self):
        self.kamus = set()
        self.kamus_verba = set()

    def load_awalan(self):
        return load_kamus('awalan')

    def load_verba(self):
        return load_kamus('verba')

    def predict(self, kata, kata_next):
        in_kamus = kata in self.kamus
        in_kamus_verba = kata_next in self.kamus_verba
        if in_kamus and in_kamus_verba:
            return False
        return True

    def fit(self):
        self.kamus = self.load_awalan()
        self.kamus_verba = self.load_verba()