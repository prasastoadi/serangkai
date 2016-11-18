from ...kamus import load_kamus

KECUALI = {'maha'}
class Terikat:

    def __init__(self):
        self.kamus = set()
        self.kamus_dasar = set()

    def load_terikat(self):
        return load_kamus('terikat')

    def load_dasar(self):
        return load_kamus('dasar')

    def pengecualian(self, kata, kata_next):
        if kata == 'maha': 
            if kata_next == 'esa':
                return True
            if kata_next in self.kamus_dasar:
                return False
        return False

    def predict(self, kata, kata_next):
        if kata in self.kamus:
            if kata in KECUALI:
                pengecualian = self.pengecualian(kata, kata_next)
                if pengecualian:
                    return True   
            return False
        return True

    def fit(self):
        self.kamus = self.load_terikat()
        self.kamus_dasar = self.load_dasar()
