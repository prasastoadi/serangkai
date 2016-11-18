import os
import sys
import polib
import argparse
from serangkai.models import Depan
from serangkai.models.rules import Awalan, Terikat, Preposisi

def get_po(filepath):
    return polib.pofile(filepath)

def main(filepath):
    depan = Depan()
    depan.fit(rules=[Awalan, Terikat, Preposisi])

    po = get_po(filepath)
    counter = 0

    for entry in po:  
        prediction = depan.predict(entry.msgstr) 

        if prediction:
            counter += 1
            print("{0}. Potensi kesalahan kata pada baris {1} !".format(counter, entry.linenum))
            for idx, kata in prediction:
                print("| kata ke-{0} : {1} ".format(idx, kata), end="")
            print("")
                
            print("msgid : {0}".format(entry.msgid))
            print("msgstr : {0}".format(entry.msgstr))
            print("_________________________________")

    print("File : {0}".format(os.path.abspath(filepath)))
    print("Total potensi kesalahan msgstr : {0}".format(counter))

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required = True,
        help = "input a po file")
    args = vars(ap.parse_args())
    
    main(args["input"])

        
    
    