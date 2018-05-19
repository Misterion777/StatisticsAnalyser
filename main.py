from continious import *
from discrete import *
from parser import *


def main():
    curr_column = 0

    datalist = pandas.read_csv("final_data.csv", header=0, usecols=[curr_column]).values.tolist()
    datalist = format_list(datalist)

    datalist.sort()

    cv1 = ContiniousVariable(datalist)
    print("---------------")
    cv2 = DiscreteVariable(datalist)


if __name__ == '__main__':
    main()