import re
from ...kamus import load_kamus

class Preposisi:

    def __init__(self):
        self.kamus = set()
        self.kamus_verba = set()
        self.kamus_dasar = set()
        self.kamus_preposisi = set()

    def load_dasar(self):
    	return load_kamus('dasar')

    def load_nomina(self):
        return load_kamus('nomina')

    def load_preposisi(self):
        return load_kamus('awalan')

    def load_verba(self):
        return load_kamus('verba')

    def predict(self, kata):

        if kata in self.kamus_dasar or kata in self.kamus_verba:
        	return True

        katak = ''
        matches = re.match(r'^(.*)(i|kan)$', kata[2:])
        if matches:
            katak = matches.group(1)

        matches2 = re.match(r'^(.*)(an)$', kata[2:])
        if matches2:
            katak2 = matches2.group(1)

        if matches and (katak in self.kamus_dasar or katak in self.kamus_verba or katak in self.kamus_nomina):
            return True

        if matches2 and (katak2 in self.kamus_dasar or katak2 in self.kamus_verba or katak2 in self.kamus_nomina):
            return True

        in_kamus_verba = kata[2:] in self.kamus_verba
        in_kamus_dasar = kata[2:] in self.kamus_dasar
        
        if in_kamus_verba or in_kamus_dasar:
            return True 

        if kata[2:] in self.kamus_nomina:
            return False

        ke = ''
        matchesk = re.match(r'^(ke|per)(.*)$', kata[2:])
        if matchesk:
            ke = matchesk.group(2)

        if matchesk and (ke in self.kamus_verba or ke in self.kamus_dasar or ke in self.kamus_nomina):
            return True

        if matches and matchesk:
            matcheske2 = re.match(r'^(.*)(i|kan)$', ke)
            ke2 = ''
            if matcheske2:
                ke2 = matcheske2.group(1)

            if ke2 in self.kamus_nomina or ke2 in self.kamus_verba or ke2 in self.kamus_dasar:
                return True

        return False

    def fit(self):
        self.kamus = self.load_preposisi()
        self.kamus_verba = self.load_verba()
        self.kamus_dasar = self.load_dasar()
        self.kamus_nomina = self.load_nomina()