from variable import *
from operator import itemgetter
from group import *


class ContiniousVariable(Variable):
    def __init__(self, datalist):
        super().__init__(datalist)

        self.range = max(self.data_set,key=itemgetter(0))[0] - min(self.data_set,key=itemgetter(0))[0]

        self.groups = self.get_groups()

        self.count_expectation()
        self.count_variance()
        self.count_deviation()

        print(self.count_ratio())

        print(self.expectation)
        print(self.variance)
        print(self.standart_deviation)


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
                group.set_characteristics()
                intervals.append(group)

                group = Group()
                left += delta

            group.add((value, frequency))

        group.set_characteristics()
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
        for (value, frequency) in self.data_set:
            self.expectation += value * frequency

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


