import matplotlib.pyplot as plt
import numpy as np
from variable import *
from operator import itemgetter
from group import *
import distributions as dists
import math_utils as mu
import scipy.stats


class ContiniousVariable(Variable):
    def __init__(self, datalist):
        super().__init__(datalist)

        self.range = max(self.data_set,key=itemgetter(0))[0] - min(self.data_set,key=itemgetter(0))[0]

        self.groups = self.get_groups()

        self.count_expectation()
        self.count_variance()
        self.count_deviation()
        self.fixed_deviation = math.sqrt(self.get_fixed_variance())

        norm = dists.Normal(self.expectation, self.fixed_deviation)
        expon = dists.Exponential(self.expectation)
        uniform = dists.Uniform(self.expectation, self.standart_deviation)

        dists_to_check = [norm, expon, uniform]

        for dist in dists_to_check:
            if mu.pearson_test(dist, self.groups, self.datalist_len):
                p_result = ''
            else:
                p_result = 'no'
            if mu.romanovsky_test(dist, self.groups, self.datalist_len):
                r_result = ''
            else:
                r_result = 'no'
            print("According to Pearson, current dataset has {} {} distribution".format(p_result,str(dist)))
            print("According to Romanovsky, current dataset has {} {} distribution".format(r_result, str(dist)))

        print(self.expectation)
        print(self.variance)
        print(self.standart_deviation)
        self.plot_data()


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

        return result / self.datalist_len


    def count_variance(self):
        between_intervals_variance = self.get_between_groups_variance()

        average_interval_variance = self.get_average_group_variance()

        self.variance = between_intervals_variance + average_interval_variance


    def count_ratio(self):
        return self.get_between_groups_variance() / self.variance


    def get_fixed_variance(self):
        return self.variance * self.datalist_len / (self.datalist_len - 1)


    def plot_data(self):
        plt.hist(self.datalist, density=True)
        plt.show()





