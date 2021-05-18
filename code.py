import pandas as pd
import plotly.express as px
import csv
import statistics
import plotly.figure_factory as ff
import random

df = pd.read_csv("data2.csv")
data = df["reading_time"].tolist()
population_mean = statistics.mean(data)
population_std = statistics.stdev(data)
print(population_mean)
print(population_std)
#population distribution curve is seen because of insuffiecient data
fig = ff.create_distplot([data],["reading_time"],show_hist = False)
fig.show()


#now making a sampling mean distribution with enough no.of data
def random_set_of_means(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean  = statistics.mean(dataSet)
    std = statistics.stdev(dataSet)
    #print(mean)
    #print(std)
    return mean
#showFig creates a graph for this and now this is normally distributed
def showFig(mean_list):
    df = mean_list
    figure = ff.create_distplot([df],["reading_time"],show_hist = False)
    figure.show()
#function to get mean of 100 data points 1000 times and plot the graph 
def setup():
    mean_list = []
    for i in range(0,1000):
        #calls the random_set_of_means def 
        set_of_means =  random_set_of_means(100)
        mean_list.append(set_of_means)
    showFig(mean_list)
def std():
    mean_list = []
    for i in range(0,1000):
        set_of_means =  random_set_of_means(100)
        mean_list.append(set_of_means)
    standardDeviation = statistics.stdev(mean_list)
    print(standardDeviation)
setup()
std()
#relationship between standard deviation of population and std of sampling mean distribution is given by 
#std of sampling mean deviation = std of population/sqrt(no of data in each sample)"""