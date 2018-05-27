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


def create_discrete_data_set(data_list,i):
    datalist = [key for key, group in groupby(data_list)]
    datafreq = [len(list(group)) for key, group in groupby(data_list)]
    df = pandas.DataFrame(dict(c1=datalist, c2=datafreq))
    df.to_csv('test_concrete_{}.csv'.format(i), header=None, index=False, sep='\t')


def create_interval_data_set(groups):
    left = []
    right = []
    freqs = []
    for group in groups:
        left.append(group.left)
        right.append(group.right)
        freqs.append(group.frequency_sum)

    df = pandas.DataFrame(dict(c1=left, c2=right, c3=freqs))
    df.to_csv('interval_test_head.csv', header=None, index=False, sep='\t')


def create_dataset():
    col1 = pandas.read_csv("Data/Concrete_data.csv", usecols=[0]).values.tolist()
    col1 = format_list(col1)

    col2 = pandas.read_csv("Data/Concrete_data.csv", usecols=[7]).values.tolist()
    col2 = format_list(col2)

    col3 = pandas.read_csv("Data/Concrete_data.csv", usecols=[8]).values.tolist()
    col3 = format_list(col3)

    df = pandas.DataFrame(dict(c1=col1, c2=col2, c3=col3))
    df.to_csv('final.csv', header=None, index=False, sep='\t')
