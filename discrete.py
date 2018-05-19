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
        for (value, frequency) in self.data_set:
            self.expectation += value * frequency

        self.expectation /= self.datalist_len

    def count_variance(self):
        for (value, frequency) in self.data_set:
            self.variance += ((value - self.expectation) ** 2) * frequency

        self.variance /= self.datalist_len

