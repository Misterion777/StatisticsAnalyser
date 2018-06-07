from continious import *
from discrete import *
from parser import *
import sys

def help():
    print("Usage: main.py <path_to_data>")
    print(r"Tip #1: if no <path_to_data> passed, default data is used (see '/Data' folder)")
    print(r"Tip #2: <path_to_data> must be csv file with no header separated by '\t' "
          r"containing 3 columns of data and at least 1000 rows")

def main(argv):
    data = 'Data/ConcreteData.csv'
    if len(argv) > 1:
        help()
        exit(1)
    elif len(argv) == 0:
        print("Passed no arguments. Using default data")
        help()
    else:
        data = argv[0]
        try:
            df = pandas.read_csv(data, header=None, sep="\t")
            if df.shape[0] < 1000 or df.shape[1] != 3:
                print("Wrong data passed! See Tip #2")
                help()
                exit(1)
        except:
            print("Wrong data passed! See Tip #2")
            help()
            exit(1)

    # FINAL

    print("-------Информация о первой колонке-------")
    datalist = pandas.read_csv(data, header=None, usecols=[0], sep="\t").values.tolist()
    datalist = format_list(datalist)
    ContiniousVariable(datalist)

    print("-------Информация о второй колонке-------")


    datalist = pandas.read_csv(data, header=None, usecols=[1], sep="\t").values.tolist()
    datalist = format_list(datalist)
    DiscreteVariable(datalist)

    print("-------Информация о третьей колонке-------")

    datalist = pandas.read_csv(data, header=None, usecols=[2], sep="\t").values.tolist()
    datalist = format_list(datalist)
    ContiniousVariable(datalist)


if __name__ == '__main__':
    main(sys.argv[1:])