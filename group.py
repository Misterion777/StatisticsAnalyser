from operator import itemgetter

class Group:
    def __init__(self):
        self.values = []

        self.average = 0
        self.frequency_sum = 0
        self.variance = 0

    def add(self, value):
        self.values.append(value)

    def __set_frequency_sum(self):
        self.frequency_sum = sum(frequency for value, frequency in self.values)

    def __set_average(self):
        self.average = sum(value * frequency for value, frequency in self.values) / self.frequency_sum

    def __set_variance(self):
        for (value, frequency) in self.values:
            self.variance += ((value - self.average) ** 2) * frequency
        self.variance /= self.frequency_sum

    def set_characteristics(self):
        self.__set_frequency_sum()
        self.__set_average()
        self.__set_variance()

