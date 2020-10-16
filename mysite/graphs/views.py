from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib, base64
import pandas as pd


def home(request):
    counter = 1;
    vals = {}
    files = ['Project6500.csv']
    types = ["line_plot", "dot_plot", "dashed_line_plot", "histogram"]
    for file in files:
        for type in types:
            vals["data" + str(counter)] =  display(file, type)
            counter += 1
    return render(request,'home.html', vals)
    
 
def display(file, type):
    series = pd.read_csv("/Users/chiragmehta/Downloads/archive/Project6500.csv", encoding= 'unicode_escape',  header=0, index_col=0, parse_dates=True, squeeze=True)
    # Loads the dataset and print the first 5 rows
    if type == "table":
        series.head()
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

    plt.xlabel('Sentiment')
    plt.ylabel('Frequency')

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    return uri