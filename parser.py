import pandas
from functools import reduce
import operator
from itertools import groupby

def limit_float(num):
    return float("{0:.4f}".format(num))

def get_formatted_column(path, column):
    col = pandas.read_csv(path, usecols=[column]).values.tolist()
    col = format_list(col)

    return col

def format_list(x):
    x = reduce(operator.concat, x)
    x = list(map(limit_float, x))
    x.sort()
    return x


def get_discrete_data_set(data_list):
    datalist = [key for key, group in groupby(data_list)]
    datafreq = [len(list(group)) for key, group in groupby(data_list)]
    return (datalist, datafreq)


def create_interval_data_set(groups):
    left = []
    right = []
    freqs = []
    for group in groups:
        left.append(group.left)
        right.append(group.right)
        freqs.append(group.frequency_sum)

    df = pandas.DataFrame(dict(c1=left, c2=right, c3=freqs))
    df.to_csv('interval_test_dasha.csv', header=None, index=False, sep='\t')


def create_dataset():
    column = 3
    gbpaud = "Data/EURCZK.csv"
    gbpdkk = "Data/EURUSD.csv"
    gbpsek = "Data/EURZAR.csv"

    data = 'final_data.csv'
    col = get_formatted_column(data, 0)




    # col1 = get_formatted_column(gbpaud, column)
    # col2 = get_formatted_column(gbpdkk, column)
    # col3 = get_formatted_column(gbpsek, column)


    df = pandas.DataFrame(dict(c1=datalist, g2=datafreq))
    df.to_csv('test_dasha.csv', header=None, index=False, sep='\t')