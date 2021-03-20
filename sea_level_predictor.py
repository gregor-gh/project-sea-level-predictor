import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", float_precision="legacy")

    # Create scatter plot
    plt.figure(figsize=(12, 6))
    g = df.plot(kind="scatter", x="Year", y="CSIRO Adjusted Sea Level")

    # Create first line of best fit
    years_extended=np.arange(1880,2050,1)
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    line = [res.slope*xi+res.intercept for xi in years_extended]
    g.plot(years_extended,line)

    df = df.loc[df["Year"]>=2000]

    # Create second line of best fit
    years_extended = np.arange(2000, 2050, 1)
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    line = [res.slope*xi+res.intercept for xi in years_extended]
    g.plot(years_extended, line)

    # Add labels and title
    g.set_xlabel("Year")
    g.set_ylabel("Sea Level (inches)")
    g.set_title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


draw_plot()
