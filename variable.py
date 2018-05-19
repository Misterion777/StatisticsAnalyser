from itertools import groupby
import math


class Variable:
    def __init__(self, datalist):

        self.data_set = []
        self.frequencies = []
        self.datalist_len = len(datalist)
        self.set_data_set(datalist)
        self.set_frequencies(datalist)

        self.expectation = 0
        self.variance = 0
        self.standart_deviation = 0

    def set_frequencies(self, data_list):
        self.frequencies = [len(list(group)) for key, group in groupby(data_list)]

    def set_data_set(self, data_list):
        self.data_set = list(set(data_list))
        self.data_set.sort()

    # СРЕДНЕВЗВЕШЕННОЕ!!!
    def count_expectation(self):
        pass

    def count_variance(self):
        pass

    def count_deviation(self):
        self.standart_deviation = math.sqrt(self.variance)