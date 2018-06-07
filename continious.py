import matplotlib.pyplot as plt
import numpy as np
from variable import *
from operator import itemgetter
from group import *
import distributions as dists
import math_utils as mu
import scipy.stats
import parser

class ContiniousVariable(Variable):
    def __init__(self, datalist):
        super().__init__(datalist)


        self.range = max(self.data_set,key=itemgetter(0))[0] - min(self.data_set,key=itemgetter(0))[0]

        self.groups = self.get_groups()

        self.output_intervals()

        print("--Основные данные--")

        self.count_expectation()
        self.count_variance()
        self.count_deviation()
        self.fixed_deviation = math.sqrt(self.get_fixed_variance())

        norm = dists.Normal(self.datalist, self.expectation, self.fixed_deviation)
        expon = dists.Exponential(self.datalist, self.expectation)
        uniform = dists.Uniform(self.datalist, self.expectation, self.standart_deviation)

        print("Оценка мат. ожидания = {}".format(self.expectation))
        print("Дисперсия = {}".format(self.variance))
        print("Среднеквадратичное отклонение = {}".format(self.standart_deviation))

        self.plot_histogram()

        dists_to_check = [norm, expon, uniform]

        print("---Критерий Пирсона---")
        for dist in dists_to_check:
            dist.plot_data()
            mu.pearson_test(dist, self.groups, self.datalist_len)

        print("---Критерий Ястремского---")
        for dist in dists_to_check:
            mu.yastremsky_test(dist, self.groups, self.datalist_len)

        plt.legend(loc='best')
        plt.show()

    def output_intervals(self):
        print("--Интервалы--")
        print("Л. граница -- Пр. граница -- Сумма частот")
        for group in self.groups:
            print("{} -- {} -- {}".format(group.left, group.right, group.frequency_sum))


    def get_delta(self):
        STURGIS_COEFFICIENT = 3.322
        return self.range / (1 + STURGIS_COEFFICIENT * math.log10(self.datalist_len))


    def get_groups(self):
        intervals = []
        delta = self.get_delta()
        left = min(self.data_set, key=itemgetter(0))[0]

        group = Group()
        for (value, frequency) in self.data_set:

            if value > left + delta:
                group.set_characteristics(left, left + delta)
                intervals.append(group)

                group = Group()
                left += delta

            group.add((value, frequency))

        group.set_characteristics(left, left + delta)
        intervals.append(group)

        return intervals


    # Средняя из внутригрупповых дисперсий
    def get_average_group_variance(self):
        result = 0
        for group in self.groups:
            result += group.variance * group.frequency_sum
        print("Средняя из внутригрупповых дисперсий = {}".format(result / self.datalist_len))
        return result / self.datalist_len


    # Общая средняя
    def count_expectation(self):
        for group in self.groups:
            self.expectation += group.middle * group.frequency_sum

        self.expectation /= self.datalist_len

    # Межгрупповая дисперсия
    def get_between_groups_variance(self):
        result = 0
        for group in self.groups:
            result += (group.average - self.expectation) ** 2 * group.frequency_sum
        print("Межгрупповая дисперсия = {}".format(result / self.datalist_len))
        return result / self.datalist_len


    def count_variance(self):
        between_intervals_variance = self.get_between_groups_variance()

        average_interval_variance = self.get_average_group_variance()

        self.variance = between_intervals_variance + average_interval_variance
        print("Межгрупповая дисперсия + средняя внутригрупповых = {}".format(self.variance))


    def count_ratio(self):
        print("{}".format(self.get_between_groups_variance() / self.variance))
        return self.get_between_groups_variance() / self.variance


    def get_fixed_variance(self):
        return self.variance * self.datalist_len / (self.datalist_len - 1)


    def plot_histogram(self):
        plt.hist(self.datalist, density=True)








