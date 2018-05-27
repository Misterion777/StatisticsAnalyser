from continious import *
from discrete import *
from parser import *


def main():
    data = 'dasha_final.csv'

    # DASHA

    datalist = pandas.read_csv(data, header=None, usecols=[0], sep='\t').values.tolist()
    datalist = format_list(datalist)
    ContiniousVariable(datalist)


    datalist = pandas.read_csv(data, header=None, usecols=[1], sep='\t').values.tolist()
    datalist = format_list(datalist)
    ContiniousVariable(datalist)


    datalist = pandas.read_csv(data, header=None, usecols=[2], sep='\t').values.tolist()
    datalist = format_list(datalist)
    DiscreteVariable(datalist)


    # FINAL


    #
    # datalist = pandas.read_csv("Data/Concrete_data.csv", header=0, usecols=[0]).values.tolist()
    # datalist = format_list(datalist)
    # ContiniousVariable(datalist)
    #
    # print("---------------")
    #
    # datalist = pandas.read_csv("Data/Concrete_data.csv", header=0, usecols=[1]).values.tolist()
    # datalist = format_list(datalist)
    # DiscreteVariable(datalist)
    #
    # print("---------------")
    #
    # datalist = pandas.read_csv("Data/Concrete_data.csv", header=0, usecols=[2]).values.tolist()
    # datalist = format_list(datalist)
    # ContiniousVariable(datalist)
    #
    # print("---------------")


if __name__ == '__main__':
    main()