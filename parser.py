import pandas
from functools import reduce
import operator

def limit_float(num):
    return float("{0:.4f}".format(num))

def get_formatted_column(path, column):
    col = pandas.read_csv(path, usecols=[column]).values.tolist()
    col = format_list(col)
    return col


def format_list(x):
    x = reduce(operator.concat, x)
    x = list(map(limit_float, x))
    return x


def create_dataset():
    column = 3
    gbpaud = "Data/EURCZK.csv"
    gbpdkk = "Data/EURUSD.csv"
    gbpsek = "Data/EURZAR.csv"

    col1 = get_formatted_column(gbpaud, column)
    col2 = get_formatted_column(gbpdkk, column)
    col3 = get_formatted_column(gbpsek, column)

    df = pandas.DataFrame(dict(gbpaud=col1, gbpdkk=col2, gbpsek=col3))
    df.to_csv('final_data_dasha1.csv', header=None, index=False)