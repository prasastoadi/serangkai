import re
      
PUNCTUATION = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
WHITESPACE = '\t\n\r\x0b\x0c'
STRIPPED = PUNCTUATION+WHITESPACE

class Preprocess:

    def __init__(self):
        pass

    def strip(self, word):
        return word.strip(STRIPPED)

    def preprocess(self, words):
        words = list(map(self.strip, self.pattern.findall(words.lower())))
        return words

    def fit(self):
        self.pattern = re.compile(r'[\w|-]+')