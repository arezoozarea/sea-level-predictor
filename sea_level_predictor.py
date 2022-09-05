import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    original_x = df["Year"]
    original_y = df["CSIRO Adjusted Sea Level"]
    plt.scatter(original_x, original_y)

    # Create first line of best fit
    mask = df["Year"] > 2000
    df = df[mask]
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

    extended_years = np.arange(2000, 2060, 10)
    predicts = [intercept + slope * new_x for new_x in extended_years]
    #
    # x = np.concatenate((x, extended_years))
    # y = np.concatenate((y, predicts))

    # slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

    # plt.plot(extended_years, predicts, 'r', label='fitted line')

    plt.plot(extended_years, predicts, 'r')
    # plt.legend()
    fmt = lambda x: "{:.1f}".format(x)

    plt.xticks(np.arange(1850, 2100, 25), [fmt(i) for i in np.arange(1850, 2100, 25)])
    plt.show()
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    # Create second line of best fit

    # Add labels and title

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
