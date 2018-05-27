from math_utils import *
import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

class Distribution:
    def __init__(self, datalist, average, deviation=None):
        self.average = average
        self.deviation = deviation
        self.datalist =datalist
        if deviation is not None:
            self.parameters_amount = 2
        else:
            self.parameters_amount = 1

    def plot_data(self):
        pass

class Normal(Distribution):
    def __init__(self, datalist, average, deviation):
        super().__init__(datalist, average, deviation)

    def get_probability(self, x1, x2=None, h=None):
        if h is not None:
            return h / self.deviation * laplace_funtion((x1 - self.average)/self.deviation)
        elif x2 is not None:
            return laplace_funtion((x2 - self.average) / self.deviation) - \
                laplace_funtion((x1 - self.average) / self.deviation)
        else:
            raise Exception("Invalid input arguments")

    def plot_data(self):
        x = np.linspace(min(self.datalist), max(self.datalist), len(self.datalist))
        dist = scipy.stats.norm
        loc_param, scale_param = dist.fit(self.datalist)
        fitted_dist = dist(loc=loc_param, scale=scale_param)

        plt.plot(x, fitted_dist.pdf(x), label='Нормальное')

    def __str__(self):
        return "нормальное"


class Exponential(Distribution):
    def __init__(self, datalist, average):
        super().__init__(datalist, average)
        self.param = 1 / self.average

    def get_probability(self, x1, x2):
        return math.exp(-1 * self.param * x1) - math.exp(-1 * self.param * x2)

    def plot_data(self):
        x = np.linspace(min(self.datalist), max(self.datalist), len(self.datalist))
        dist = scipy.stats.expon
        loc_param, scale_param = dist.fit(self.datalist)
        fitted_dist = dist(loc=loc_param, scale=scale_param)

        plt.plot(x, fitted_dist.pdf(x), label='Экспоненциальное')

    def __str__(self):
        return "экспоненциальное"


class Uniform(Distribution):
    def __init__(self, datalist, average, deviation):
        super().__init__(datalist, average,deviation)

        self.a = self.average - math.sqrt(3 * self.deviation)
        self.b = self.average + math.sqrt(3 * self.deviation)
        self.pdf = 1 / (self.b - self.a)

    def get_probability(self, x1=None, x2=None):
        if x1 is None and x2 is not None:
            return self.pdf * (x2 - self.a)
        if x2 is None and x1 is not None:
            return self.pdf * (self.b - x1)

        if x2 is not None and x1 is not None:
            result = self.pdf * (x2 - x1)
            if result < 0:
                return 0
            else:
                return result
        else:
            raise Exception("Invalid input arguments")


    def plot_data(self):
        x = np.linspace(min(self.datalist), max(self.datalist), len(self.datalist))
        dist = scipy.stats.uniform
        loc_param, scale_param = dist.fit(self.datalist)
        fitted_dist = dist(loc=loc_param, scale=scale_param)

        plt.plot(x, fitted_dist.pdf(x), label='Равномерное')

    def __str__(self):
        return "равномерное"


class Binomial(Distribution):
    def __init__(self, datalist, average, n):
        super().__init__(datalist, average)
        self.n = n
        self.parameters_amount = 2
        self.p = (self.average / self.n)

    def get_probability(self, x):
        return scipy.stats.binom.pmf(x,self.n,self.p)

    def plot_data(self):
        x = np.arange(min(self.datalist), max(self.datalist))
        plt.plot(x, scipy.stats.binom.pmf(x, self.n, self.p), label='Бернулли')

    def __str__(self):
        return "биномиальное"


class Geometric(Distribution):
    def __init__(self, datalist, average):
        super().__init__(datalist, average)
        self.p = 1 / (self.average + 1)


    def plot_data(self):
        x = np.arange(min(self.datalist), max(self.datalist))
        plt.plot(x, scipy.stats.geom.pmf(x, self.p), label='Геометрическое')


    def get_probability(self, x):
        return scipy.stats.geom.pmf(x, self.p)

    def __str__(self):
        return "геометрическое"


class Poisson(Distribution):
    def __init__(self, datalist, average):
        super().__init__(datalist, average)

    def plot_data(self):
        x = np.arange(min(self.datalist), max(self.datalist))
        plt.plot(x, scipy.stats.poisson.pmf(x, self.average), label='Пуассон')


    def get_probability(self, i):
        return scipy.stats.poisson.pmf(i, self.average)

    def __str__(self):
        return "пуассоновское"