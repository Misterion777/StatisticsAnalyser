from variable import *
from operator import itemgetter

class ContiniousVariable(Variable):
    def __init__(self, datalist):
        super().__init__(datalist)

        self.range = max(self.data_set,key=itemgetter(0))[0] - min(self.data_set,key=itemgetter(0))[0]

        self.intervals = self.get_intervals()

        self.count_expectation()
        self.count_variance()
        self.count_deviation()

        print(self.expectation)
        print(self.variance)
        print(self.standart_deviation)



    def get_delta(self):
        STURGIS_COEFFICIENT = 3.322
        return self.range / (1 + STURGIS_COEFFICIENT * math.log10(self.datalist_len))


    def get_intervals(self):
        intervals = []
        delta = self.get_delta()
        left = min(self.data_set, key=itemgetter(0))[0]

        frequency_sum = 0
        for (value, frequency) in self.data_set:
            if value > left + delta:
                intervals.append((left, left + delta, frequency_sum))
                left += delta
                frequency_sum = 0

            frequency_sum += frequency

        intervals.append((left, left+delta, frequency_sum))
        return intervals


    # СРЕДНЕВЗВЕШЕННОЕ!!!
    def count_expectation(self):

        for (left, right, frequency) in self.intervals:
            mid = (left + right) / 2
            self.expectation += mid * frequency

        self.expectation /= self.datalist_len

    def count_variance(self):

        for (left, right, frequency) in self.intervals:
            mid = (left + right) / 2
            self.variance += ((mid - self.expectation)**2) * frequency

        self.variance /= self.datalist_len
