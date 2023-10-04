import matplotlib.pyplot as plt
from load_csv import load


def main():
    """loads the csv file and find Malaysia in the index and plots it
pandas has an inbuilt plot function that uses matplotlib,
so you dont have to use plt.plot"""
    ley = load("life_expectancy_years.csv")
    my_country_name = 'South Korea'
    # print(ley)
    country_info = ley.loc[my_country_name]
    # print(country_info, type(country_info))
    country_info.plot(
        xlabel="Year",
        ylabel="Life Expectancy",
        title=f"{my_country_name} Life Expectancy Projections",
    )
    plt.show()


if __name__ == "__main__":
    main()
