import pandas as pd
import matplotlib.pyplot as plt

info = pd.read_csv('/content/world_population.csv')
data = info.head()
print(data)


dis = info.tail(10)
color = ['orange']
plt.bar(dis['CCA3'],dis['2022 Population'],color=color)
plt.title(" Population of 10 countries of the world in the year 2022  ")


dis = info.head(25)
color = ['grey']
plt.hist(dis['2000 Population'],color=color)
plt.title("Population of 25 countries of the world in the year 2000 through HISTOGRAM")

dis = info.tail(50)
color = ['pink']
plt.hist(dis['1970 Population'],color=color)
plt.title("Population of 50 countries of the world in the year 1970 through HISTOGRAM")


dis = info.head(100)
color = 'Red'
plt.bar(dis['Rank'],dis['World Population Percentage'],color=color)
plt.title("Population % of countries of the world")
plt.xlabel('Rank')
plt.ylabel('World Population Percentage')
