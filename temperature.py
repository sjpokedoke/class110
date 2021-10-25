import csv
import plotly.figure_factory as ff
import pandas as pd
import statistics
import random

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

def randomsetofmean(count):
    dataset = []
    for i in range(0, count):
        randomindex = random.randint(0, len(data)-1)
        value = data[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def showfig(meanlist):
    df = meanlist
    mean = statistics.mean(meanlist)
    stdev = statistics.stdev(meanlist)
    print("Mean is: "+ str(mean))
    print("Standard deviation is: "+ str(stdev))
    fig = ff.create_distplot([df], ["Temperature"], show_hist = False)
    fig.show()

def setup():
    meanlist = []
    for i in range(0, 1000):
        setofmeans = randomsetofmean(100)
        meanlist.append(setofmeans)
    showfig(meanlist)

setup()