from variable import *


class DiscreteVariable(Variable):
    def __init__(self, datalist):
        super().__init__(datalist)

        self.count_expectation()
        self.count_variance()
        self.count_deviation()

        print(self.expectation)
        print(self.variance)
        print(self.standart_deviation)

    # СРЕДНЕВЗВЕШЕННОЕ!!!
    def count_expectation(self):
        i = 0
        for value in self.data_set:
            self.expectation += value * self.frequencies[i]
            i += 1

        self.expectation /= self.datalist_len

    def count_variance(self):
        i = 0
        for value in self.data_set:
            self.variance += ((value - self.expectation) ** 2) * self.frequencies[i]
            i += 1

        self.variance /= self.datalist_len

