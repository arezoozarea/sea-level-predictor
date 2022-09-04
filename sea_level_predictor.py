import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    df = df.append({"Year": 2050, "CSIRO Adjusted Sea Level":0}, ignore_index=True)
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    plt.scatter(x, y)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

    extended_years = np.arange(2000, 2050, 10)
    predicts = [intercept + slope * new_x for new_x in extended_years]

    plt.plot(extended_years, predicts, 'r', label='fitted line')
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.show()
    # Create second line of best fit

    # Add labels and title

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
