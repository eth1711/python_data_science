import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd


def main():
    """loads the csv file and takes two countries from the
csv file and plots it. loc is used to locate in a column
iterrows returns an index and a string, so when i give it a dataframe,
it converts it to a series, then i plot it out through the for loops"""
    pop = load("population_total.csv")
    my_country_name = 'Belgium'
    enemy_country_name = 'France'
    # print(pop)
    country_info = pop.loc[[my_country_name, enemy_country_name], :'2050']
    country_info.replace(
        {'k': '*1e3', 'M': '*1e6', 'B': '*1e9'}, regex=True, inplace=True)
    country_info = country_info.apply(pd.eval)
    # print(country_info, type(country_info))
    for i, s in country_info.iterrows():
        print(s)
        plt.plot(s.index.astype(int), s.values.astype(int), label=i)
    plt.legend()
    ticks, labels = plt.yticks()
    plt.yticks(ticks[1:], [f"{int(x / 1000000)}M" for x in ticks[1:]])
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population Projection")
    plt.show()


if __name__ == "__main__":
    main()
