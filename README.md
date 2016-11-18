# Serangkai
A simple library to detect grammar error in Bahasa Indonesia.

Create a new object and then fit the rules:

      depan = Depan()
      depan.fit(rules=[Awalan, Terikat, Preposisi])

Feed a sentence to predict-function:

      po = get_po(filepath)
      for entry in po:  
          prediction = depan.predict(entry.msgstr) 
          ...
          
depan.predict(text) returns list of tuple (index, kata). Index is the position of kata (the word where potential error arises) in the text.

An example can be found in demo.py

#### License

This library is licensed under [The MIT License (MIT)](https://opensource.org/licenses/MIT).

Kamus (vocabularies data) are extracted from Kateglo. Licensed under [CC-BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/).
