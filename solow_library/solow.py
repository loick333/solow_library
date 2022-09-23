import numpy as np
import matplotlib.pyplot as plt
import doctest

# Constants constants

KAPITAL_0 = 1
POP_0 = 1

class Economy:
    """
    Represents a certain area's economy

    Instance Attributes: name (str), savings (float), depreciation (float),
                         population_growth (float), capital_ratio (float), time (int)
    """

    def __init__(self, name="Canada", savings=0.3, depreciation=0.03,
                 population_growth=0.02, capital_ratio=0.3, time=2):
        self.name = name
        self.savings = savings
        self.depreciation = depreciation
        self.population_growth = population_growth
        self.capital_ratio = capital_ratio
        self.time = time

    def __str__(self):
        """
        (Economy) -> str

        >>> canada = Economy()
        >>> print(canada)
        Canada
        Savings: 0.3
        Depreciation: 0.03
        Population Growth: 0.02
        Capital Ratio: 0.3
        """
        info = self.name + "\nSavings: " + str(self.savings) + "\nDepreciation: " + str(self.depreciation) \
               + "\nPopulation Growth: " + str(self.population_growth) + "\nCapital Ratio: " + str(self.capital_ratio)
        return info

    def capital_capita(self):
        """
        (Economy) -> tuple(float, list, list, list)

        >>> canada = Economy()
        >>> result = canada.capital_capita()
        >>> result[0] == result[1][-1]
        True
        >>> print(result[1])
        [1.25, 1.5082703799973565]
        >>> print(result[2])
        [0.25, 0.20661630399788514]
        >>> print(result[3])
        [1, 2]
        """
        s = self.savings
        d = self.depreciation
        n = self.population_growth
        a = self.capital_ratio
        t = self.time

        return Economy.get_capital_capita(t, s, d, n, a)

    def output_capita(self):
        """
        (Economy) -> list

        This method takes as input and Economy object and
        outputs a list representing output per capita for each time t.

        >>> canada = Economy()
        >>> print(canada.output_capita())
        [1.069234599991188, 1.131211367506459]
        >>> usa = Economy(capital_ratio=0.4)
        >>> print(usa.output_capita())
        [1.0933620739432781, 1.1809278496201596]
        """
        s = self.savings
        d = self.depreciation
        n = self.population_growth
        a = self.capital_ratio
        t = self.time

        return Economy.get_output_capita(t, s, d, n, a)

    def output_capita_growth(self):
        """
        (float, float, float, float, float) -> float

        This method takes as input floats describing economic variables and
        inputs the change in Capital from time t to t+1.

        >>> canada = Economy()
        >>> print(canada.output_capita())
        [1.069234599991188, 1.131211367506459]
        >>> usa = Economy(capital_ratio=0.4)
        >>> print(usa.output_capita())
        [1.0933620739432781, 1.1809278496201596]
        """
        s = self.savings
        d = self.depreciation
        n = self.population_growth
        a = self.capital_ratio
        t = self.time
        return Economy.get_capital_capita(t, s, d, n, a)

    def kapital_plot(self):
        s = self.savings
        d = self.depreciation
        n = self.population_growth
        a = self.capital_ratio
        t = self.time
        plt.plot(Economy.get_capital_capita(t, s, d, n, a)[3], Economy.get_capital_capita(t, s, d, n, a)[1])
        plt.show()

    def kapital_g_plot(self):
        s = self.savings
        d = self.depreciation
        n = self.population_growth
        a = self.capital_ratio
        t = self.time
        plt.plot(Economy.get_capital_capita(t, s, d, n, a)[3], Economy.get_capital_capita(t, s, d, n, a)[2])
        plt.show()

    def wage(self):
        """
        (int, float, float, float, float) -> list

        This method takes as input floats describing economic variables and
        outputs a list representing wages for every t.

        >>> canada = Economy()
        >>> print(canada.wage())
        [0.7484642199938315, 0.7918479572545214]
        >>> usa = Economy(capital_ratio=0.4)
        >>> print(usa.wage())
        [0.6560172443659669, 0.7085567097720957]
        """
        s = self.savings
        d = self.depreciation
        n = self.population_growth
        a = self.capital_ratio
        t = self.time
        return Economy.get_wage(t, s, d, n, a)

    def interest_rate(self):
        """
        (int, float, float, float, float) -> list

        This method takes as input floats describing economic variables and
        outputs a list containin the interest rate for each time t.

        >>> canada = Economy()
        >>> print(canada.interest_rate())
        [0.2266163039978851, 0.1950017070895024]
        >>> usa = Economy(savings=0.4)
        >>> print(usa.interest_rate())
        [0.21315747043437466, 0.17521963923411402]
        """
        s = self.savings
        d = self.depreciation
        n = self.population_growth
        a = self.capital_ratio
        t = self.time

        # Use Cobb-Douglas Function
        return Economy.get_interest_rate(t, s, d, n, a)

    def plot_all(self):
        s = self.savings
        d = self.depreciation
        n = self.population_growth
        a = self.capital_ratio
        t = self.time
        return Economy.get_plot_all(t, s, n, d, a)

    @staticmethod
    def get_kapital_dot(k, s, d, n, a):
        """
        (float, float, float, float, float) -> float

        This method takes as input floats describing economic variables and
        inputs the change in Capital from time t to t+1.

        >>> print(round(Economy.get_kapital_dot(1, 0.3, 0.03, 0.02, 0.3), 2))
        0.25
        >>> print(round(Economy.get_kapital_dot(2, 0.3, 0.03, 0.02, 0.3), 2))
        0.27
        """
        # Definition of ODE
        return s * (k ** a) - (n + d) * k

    # Solution to Diff equation
    @staticmethod
    def get_capital_capita(t, s, d, n, a):
        """
        (float, float, float, float, float) -> float

        This method takes as input floats describing economic variables and
        inputs the change in Capital from time t to t+1.

        >>> result = Economy.get_capital_capita(2, 0.3, 0.03, 0.02, 0.3)
        >>> result[0] == result[1][-1]
        True
        >>> print(result[1])
        [1.25, 1.5082703799973565]
        >>> print(result[2])
        [0.25, 0.20661630399788514]
        >>> print(result[3])
        [1, 2]
        """
        year = []
        capital_list = []
        capital_g_list = []
        # Initialize changing values
        k = KAPITAL_0
        delta_t = 1
        current_year = 0
        for time in np.arange(current_year, t, delta_t):
            capital_g_list.append(Economy.get_kapital_dot(k, s, d, n, a) / k)
            k += Economy.get_kapital_dot(k, s, d, n, a)  # * delta_t

            current_year += delta_t
            year.append(current_year)
            capital_list.append(k)

        return k, capital_list, capital_g_list, year

    @staticmethod
    def get_output_capita(t, s, d, n, a):
        """
        (float, float, float, float, float) -> float

        This method takes as input floats describing economic variables and
        inputs the change in Capital from time t to t+1.

        >>> print(Economy.get_output_capita(2, 0.3, 0.03, 0.02, 0.3))
        [1.069234599991188, 1.131211367506459]
        >>> print(Economy.get_output_capita(2, 0.4, 0.03, 0.02, 0.3))
        [1.0942086169546863, 1.1767180878835704]
        """
        capital_list = Economy.get_capital_capita(t, s, d, n, a)[1]
        output_list = []
        for k in capital_list:
            output_list.append(k ** a)

        return output_list

    @staticmethod
    def get_output_capita_growth(t, s, d, n, a):
        """
        (float, float, float, float, float) -> float

        This method takes as input floats describing economic variables and
        inputs the change in Capital from time t to t+1.

        >>> print(Economy.get_output_capita_growth(2, 0.3, 0.03, 0.02, 0.3))
        [0.05478796385496634, 0.05478796385496634]
        >>> print(Economy.get_output_capita_growth(2, 0.4, 0.03, 0.02, 0.3))
        [0.0701182991733258, 0.0701182991733258]
        """
        output_list = Economy.get_output_capita(t, s, d, n, a)
        growth_list = []
        for i in range(1, len(output_list)):
            growth = (output_list[i] - output_list[i - 1]) / output_list[i]
            growth_list.append(growth)
        growth_list.append(growth_list[-1])
        return growth_list


    @staticmethod
    def get_kapital_plot(t, s, n, d, a):
        plt.plot(Economy.get_capital_capita(t, s, d, n, a)[3], Economy.get_capital_capita(t, s, d, n, a)[1])
        plt.show()

    @staticmethod
    def get_kapital_g_plot(t, s, n, d, a):
        plt.plot(Economy.get_capital_capita(t, s, d, n, a)[3], Economy.get_capital_capita(t, s, d, n, a)[2])
        plt.show()

    @staticmethod
    def get_wage(t, s, d, n, a):
        """
        (int, float, float, float, float) -> list

        This method takes as input floats describing economic variables and
        outputs a list representing wages for every t.

        >>> print(Economy.get_wage(2, 0.3, 0.03, 0.02, 0.3))
        [0.7484642199938315, 0.7918479572545214]
        >>> print(Economy.get_wage(2, 0.4, 0.03, 0.02, 0.3))
        [0.7659460318682804, 0.8237026615184994]
        """
        # Use Cobb-Douglas Function
        capital_list = Economy.get_capital_capita(t, s, d, n, a)[1]
        pop = POP_0
        wage_list = []
        for k in capital_list:
            pop *= 1 + n
            # Multiply k by pop because
            wage_list.append((1 - a) * ((k * pop) ** a) * pop ** (-a))
        return wage_list

    @staticmethod
    def get_interest_rate(t, s, d, n, a):
        """
        (int, float, float, float, float) -> list

        This method takes as input floats describing economic variables and
        outputs a list containin the interest rate for each time t.

        >>> print(Economy.get_interest_rate(2, 0.3, 0.03, 0.02, 0.3))
        [0.2266163039978851, 0.1950017070895024]
        >>> print(Economy.get_interest_rate(2, 0.4, 0.03, 0.02, 0.3))
        [0.21315747043437466, 0.17521963923411402]
        """
        # Use Cobb-Douglas Function
        capital_list = Economy.get_capital_capita(t, s, d, n, a)[1]
        pop = POP_0
        get_interest_rate_list = []
        for k in capital_list:
            pop *= 1 + n
            get_interest_rate_list.append(a * ((k * pop) ** (a - 1)) * pop ** (1 - a) - d)
        return get_interest_rate_list

    @staticmethod
    def get_plot_all(t, s, n, d, a):
        fig, axs = plt.subplots(3, 2)
        axs[0, 0].plot(Economy.get_capital_capita(t, s, d, n, a)[3], Economy.get_capital_capita(t, s, d, n, a)[1])
        axs[0, 0].set_title('Capital Per Capita')
        axs[0, 1].plot(Economy.get_capital_capita(t, s, d, n, a)[3], Economy.get_capital_capita(t, s, d, n, a)[2])
        axs[0, 1].set_title('Capital Growth')
        axs[1, 0].plot(Economy.get_capital_capita(t, s, d, n, a)[3], Economy.get_output_capita(t, s, d, n, a))
        axs[1, 0].set_title('Output per Capita')
        axs[1, 1].plot(Economy.get_capital_capita(t, s, d, n, a)[3], Economy.get_output_capita_growth(t, s, d, n, a))
        axs[1, 1].set_title('Output Per Capita Growth')
        axs[2, 1].plot(Economy.get_capital_capita(t, s, d, n, a)[3], Economy.get_interest_rate(t, s, d, n, a))
        axs[2, 1].set_title('Interest Rate')
        axs[2, 0].plot(Economy.get_capital_capita(t, s, d, n, a)[3], Economy.get_wage(t, s, d, n, a))
        axs[2, 0].set_title('Wage')
        plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.3, hspace=0.5)
        plt.show()


if __name__ == "__main__":
    canada = Economy(time=200)
    print(canada)
    doctest.testmod()