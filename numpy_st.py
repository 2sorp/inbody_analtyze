import numpy as np
import pandas as pd

population_dict = {
    'china': 141500,
    'japan': 12718,
    'korea': 5180,
    'usa': 32676
}
population = pd.Series(population_dict)

gdp_dict = {
    'china': 1409250000,
    'japan': 516700000,
    'korea': 169320000,
    'usa': 2041280000,
}
gdp = pd.Series(gdp_dict)

country = pd.DataFrame({
    'gdp': gdp,
    'population': population
})

print(country)
