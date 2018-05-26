from math_utils import *


class Distribution:
    def __init__(self, average, deviation=None):
        self.average = average
        self.deviation = deviation
        if deviation is not None:
            self.parameters_amount = 2
        else:
            self.parameters_amount = 1


class Normal(Distribution):
    def __init__(self, average, deviation):
        super().__init__(average, deviation)

    def get_probability(self, x1, x2=None, h=None):
        if h is not None:
            return h / self.deviation * laplace_funtion((x1 - self.average)/self.deviation)
        elif x2 is not None:
            return laplace_funtion((x2 - self.average) / self.deviation) - \
                laplace_funtion((x1 - self.average) / self.deviation)
        else:
            raise Exception("Invalid input arguments")

    def __str__(self):
        return "normal"


class Exponential(Distribution):
    def __init__(self, average):
        super().__init__(average)
        self.param = 1 / self.average

    def get_probability(self, x1, x2):
        return math.exp(-1 * self.param * x1) - math.exp(-1 * self.param * x2)

    def __str__(self):
        return "exponential"


class Uniform(Distribution):
    def __init__(self, average, deviation):
        super().__init__(average,deviation)

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

    def __str__(self):
        return "uniform"


class Binomial(Distribution):
    def __init__(self, average, n):
        super().__init__(average)
        self.n = n
        self.parameters_amount = 2
        self.p = (self.average / self.n)

    def get_probability(self, x):
        c = math.factorial(self.n) / (math.factorial(x) * math.factorial(self.n - x))
        return c * (self.p ** x) * ((1 - self.p) ** (self.n - x))

    def __str__(self):
        return "binomial"


class Geometric(Distribution):
    def __init__(self, average, variance):
        super().__init__(average)
        self.variance = variance
        self.p = average / variance

    # TODO CHECK X!!!!!!
    def get_probability(self, i):
        return self.p * (1 - self.p) ** i

    def __str__(self):
        return "geometric"


class Poisson(Distribution):
    def __init__(self, average):
        super().__init__(average)


    def get_probability(self, i):
        return self.average ** i / math.factorial(i) * math.exp(-1 * self.average)

    def __str__(self):
        return "poisson"