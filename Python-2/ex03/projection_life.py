import matplotlib.pyplot as plt
from load_csv import load


def main():
    """loads the csv file and takes two countries from the
csv file and plots it. loc is used to locate in a column
iterrows returns an index and a string, so when i give it a dataframe,
it converts it to a series, then i plot it out through the for loops"""
    ley = load("life_expectancy_years.csv")
    gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    ley = ley[["1900"]]
    gdp = gdp[["1900"]]
    merge = ley.merge(gdp, on="country")
    # print(merge)
    merge.plot.scatter(
        x="1900_y",
        y="1900_x",
        xlabel="Gross Domestic Product",
        ylabel="Life Expectancy",
        logx=True,
        title="1900",
    )
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.show()


if __name__ == "__main__":
    main()
