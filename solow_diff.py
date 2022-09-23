import numpy as np
import matplotlib.pyplot as plt

# physical constants
s = 0.3
d = 0.03
n = 0.02
a = 0.3
t = 2

KAPITAL_0 = 1
POP_0 = 1

# Solution to Diff equation
def get_capital_capita(t, s, d, n, a):
    year = []
    capital_list = []
    capital_g_list = []
    # Initialize changing values
    k = KAPITAL_0
    delta_t = 1
    current_year = 0
    for time in np.arange(current_year, t, delta_t):
        capital_g_list.append((s*(k**a)-(n+d)*k)/k)
        k += s*(k**a)-(n+d)*k #* delta_t

        current_year += delta_t
        year.append(current_year)
        capital_list.append(k)

    return k, capital_list, capital_g_list, year

    """
    def capital(t, s, d, n, a):

        #lis
        year = []
        capital_list = []
        capital_g_list = []

        # Initialize changing values
        k = KAPITAL_0
        pop = POP_0
        delta_t = 1
        current_year = 0
        for time in np.arange(current_year, t, delta_t):
            pop *= 1+n
            capital_g_list.append(get_kapital_dot(k, s, d, n, a)/k)
            k = (k + get_kapital_dot(k, s, d, n, a))*pop #* delta_t

            current_year += delta_t
            year.append(current_year)
            capital_list.append(k)

        return k, capital_list, capital_g_list, year
    """

def get_output_capita(t, s, d, n, a):
    """
    (float, float, float, float, float) -> float

    This method takes as input floats describing economic variables and
    inputs the change in Capital from time t to t+1.

    >> print(get_kapital_dot(1, 0.3, 0.03, 0.02, 0.3))
    0.25
    >> print(get_kapital_dot(2, 0.3, 0.03, 0.02, 0.3))
    0.27
    """
    capital_list = get_capital_capita(t, s, d, n, a)[1]
    output_list = []
    for k in capital_list:
        output_list.append(k ** a)

    return output_list


print(get_output_capita(2, 0.3, d, n, a))