from csvreader import csv, CSVReader


class TypeFile:
    """
    define a type of file
    """

readers =   {
    '.txt':'TxtReader()',
    '.csv':'CSVReader()'
    }

def get_symb(Filename,symb):
    """
    get required symbol ii file
    :param Filename: file's name
    :param symb: required symbol
    :return: index of symb
    """
    return Filename.index(symb)

def get_reader(Filename):
    """
    get suitable reader to file type
    :param Filename: file's name
    :return: suitable reader
    """
    return readers.get(Filename[get_dot(Filename,'.'):])



