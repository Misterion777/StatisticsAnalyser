import scipy
import scipy.stats
import math


ALPHA = 0.05


# values are values + weights
def count_weighted_average(values, n):
    return sum(value * weight for value, weight in values) / n


def laplace_funtion(x):
    return scipy.stats.norm.cdf(x) - 0.5


def yastremsky_test(distribution, values, n):
    chi = chi_square(distribution, values, n)

    degrees_of_freedom = len(values) - distribution.parameters_amount - 1

    r = abs(chi - degrees_of_freedom) / math.sqrt(2 * len(values) + 2.4)

    print(str(distribution))
    print("R = {}".format(r))

    return r < 3

def romanovsky_test(distribution, values, n):
    chi = chi_square(distribution, values, n)

    degrees_of_freedom = len(values) - distribution.parameters_amount - 1

    r = abs(chi - degrees_of_freedom) / math.sqrt(2 * degrees_of_freedom)

    print(str(distribution))
    print("R = {}".format(r))

    return r < 3


def pearson_test(distribution, values, n):
    chi = chi_square(distribution, values, n)

    degrees_of_freedom = len(values) - distribution.parameters_amount - 1

    from_table = scipy.stats.chi2.isf(ALPHA, degrees_of_freedom)

    print(str(distribution))
    print("Хи квадрат наблюдаемое = {}".format(chi))
    print("Хи квадрат теоретическое = {}".format(from_table))
    return chi < from_table


def chi_square(distribution, values, n):
    if str(distribution) in ['пуассоновское','геометрическое', 'биномиальное']:
        return __discrete_chi(values, n, distribution)
    if str(distribution) == 'равномерное':
        return __uniform_chi(distribution, values, n)
    else:
        return __other__chi([(group.left, group.right, group.frequency_sum) for group in values], n, distribution)

def __iterative_chi(values, n, distribution):
    result = 0
    i = 0
    for x, f in values:
        theoretical_frequency = n * \
                                distribution.get_probability(i)

        try:
            result += (f - theoretical_frequency) ** 2 / theoretical_frequency
        except RuntimeWarning:
            result += 0
        i += 1
    return result


def __other__chi(values, n, distribution):
    result = 0
    for x1, x2, f in values:
        theoretical_frequency = n * \
                                distribution.get_probability(x1, x2)

        result += (f - theoretical_frequency) ** 2 / theoretical_frequency
    return result


def __discrete_chi(values, n, distribution):
    result = 0
    for x, f in values:
        theoretical_frequency = n * \
                                distribution.get_probability(x)

        result += (f - theoretical_frequency) ** 2 / theoretical_frequency
    return result

def __uniform_chi(distribution, groups, n):
    result = 0

    for group in groups:
        if groups.index(group) == 0:
            theoretical_frequency = n * \
                                distribution.get_probability(x2=group.right)
        elif groups.index(group) == len(groups):
            theoretical_frequency = n * \
                                    distribution.get_probability(x1=group.left)
        else:
            theoretical_frequency = n * \
                                    distribution.get_probability(group.left, group.right)

        result += (group.frequency_sum - theoretical_frequency) ** 2 / theoretical_frequency

    return result





