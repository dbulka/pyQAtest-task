import csv


class CSVReader(object):
    """
    csvfiles reader
    """

    def __init__(self):
        """
        initialize new csvreader
        """

    def read(self, Filename):
        """
        read a csv file
        :param Filename: file name
        :return: x,y - points of axis
        """
        x = []
        y = []
        with open(Filename, newline='') as file:
            for row in csv.reader(file):
                print(row)
                str(row).split(';')
                x.append(row[0])
                print(x)
                y.append(row[1])
                print(y)
        return x,y

print(csv.__file__)
csv = CSVReader()
csv.read('points_sheet.csv')

