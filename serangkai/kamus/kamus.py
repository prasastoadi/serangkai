import os
import codecs
import csv

PATH_KATA_DASAR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "kamus-kata-dasar.csv")
PATH_KATA_TERIKAT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "kamus-kata-terikat.csv")
PATH_KATA_VERBA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "kamus-kata-verba.csv")
PATH_KATA_AWALAN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "kamus-kata-awalan.csv")
PATH_KATA_NOMINA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "kamus-kata-nomina.csv")

PATH_KATA = {
    "dasar" : PATH_KATA_DASAR,
    "terikat" : PATH_KATA_TERIKAT,
    "verba" : PATH_KATA_VERBA,
    "awalan" : PATH_KATA_AWALAN,
    "nomina" : PATH_KATA_NOMINA,
    "custom" : None
}


def load_file(filepath):

    with codecs.open(filepath, mode='r', encoding='utf-8')as f:
        reader = csv.reader(f)
        for i in reader:
            yield i[0]

def load_kamus(kata, filepath=None):

    if kata == 'custom':
        PATH_KATA[kata] = filepath

    try:
        path = PATH_KATA[kata]
    except KeyError:
        raise ValueError("Kelas invalid")

    kamus = set(load_file(path))

    return kamus


