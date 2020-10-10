from pandas import read_csv
from matplotlib import pyplot


# Loads the dataset and print the first 5 rows
def display(file, type):
    series = read_csv(file, encoding="ISO-8859-1", header=0, index_col=0, parse_dates=True, squeeze=True)
    # Loads the dataset and print the first 5 rows
    if type == "table":
        print(series.head())
    # Time Series Line Plot
    elif type == "line_plot":
        series.plot()
    # Time Series Dot Plot (Modified Line Plot where style of line is black dots)
    elif type == "dot_plot":
        series.plot(style='k.')
    # Time Series Dashed Line Plot (Modified Line Plot where style of line is dashed lines)
    elif type == "dashed_line_plot":
        series.plot(style='k-')
    # Time Series Histogram where sentiment values are grouped into bins and the vertical axis is the frequency of each sentiment
    elif type == "histogram":
        series.hist()
    pyplot.show()


files = ['Project6500.csv', 'reuters_data.csv']
types = ["table", "line_plot", "dot_plot", "dashed_line_plot", "histogram"]
for file in files:
    for type in types:
        display(file, type)
