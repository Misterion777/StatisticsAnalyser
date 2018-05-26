from variable import *
import distributions as dists
import math_utils as mu
import matplotlib.pyplot as plt


class DiscreteVariable(Variable):
    def __init__(self, datalist):
        super().__init__(datalist)

        self.count_expectation()
        self.count_variance()
        self.count_deviation()

        self.plot_data()

        geom = dists.Geometric(self.expectation, self.variance)
        binom = dists.Binomial(self.expectation, self.datalist_len)
        pois = dists.Poisson(self.expectation)

        dists_to_check = [geom, binom, pois]

        for dist in dists_to_check:
            if mu.pearson_test(dist, self.data_set, self.datalist_len):
                p_result = ''
            else:
                p_result = 'no'
            if mu.romanovsky_test(dist, self.data_set, self.datalist_len):
                r_result = ''
            else:
                r_result = 'no'
            print("According to Pearson, current dataset has {} {} distribution".format(p_result, str(dist)))
            print("According to Romanovsky, current dataset has {} {} distribution".format(r_result, str(dist)))


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


    def plot_data(self):
        x = []
        y = []
        for value, freq in self.data_set:
            x.append(value)
            y.append(freq)

        plt.plot(x, y)
        plt.show()