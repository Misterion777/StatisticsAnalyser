from variable import *
import distributions as dists
import math_utils as mu
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np


class DiscreteVariable(Variable):
    def __init__(self, datalist):
        super().__init__(datalist)

        self.count_expectation()
        self.count_variance()
        self.count_deviation()

        geom = dists.Geometric(self.datalist, self.expectation)
        binom = dists.Binomial(self.datalist, self.expectation, self.datalist_len)
        pois = dists.Poisson(self.datalist, self.expectation)

        dists_to_check = [pois, geom, binom]

        self.plot_polygon()
        print("Оценка мат. ожидания = {}".format(self.expectation))
        print("Дисперсия = {}".format(self.variance))
        print("Среднеквадратичное отклонение = {}".format(self.standart_deviation))

        print("---Критерий Пирсона---")
        for dist in dists_to_check:
            dist.plot_data()
            mu.pearson_test(dist, self.data_set, self.datalist_len)

        print("---Критерий Ястремского---")
        for dist in dists_to_check:
            mu.yastremsky_test(dist, self.data_set, self.datalist_len)

        plt.legend(loc='best')
        plt.show()


    # СРЕДНЕВЗВЕШЕННОЕ!!!
    def count_expectation(self):
        for (value, frequency) in self.data_set:
            self.expectation += value * frequency

        self.expectation /= self.datalist_len

    def count_variance(self):
        for (value, frequency) in self.data_set:
            self.variance += ((value - self.expectation) ** 2) * frequency

        self.variance /= self.datalist_len


    def plot_polygon(self):
        x = []
        y = []
        for value, freq in self.data_set:
            x.append(value)
            y.append(freq / self.datalist_len)

        plt.plot(x, y)