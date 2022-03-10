import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

df = pd.read_csv('C:\\Users\\CHANDU\\Desktop\\Gold_Price_Analysis\\GoldRate_Analysis.csv')

print(df)

#color palette
colors = ["#EF233C","#eb5e28","#d68c45","#00bbf9","#274c77","#3a0ca3"]
palette = sns.color_palette(palette = colors)
sns.palplot(palette, size =1)
plt.show()

#Pie Chart
labels = 'Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday','Saturday','Sunday'
sizes = [52,52,52,52,53,52,52]
fig, ax = plt.subplots(figsize=(10,7))
fig.set_facecolor('white')
ax.pie(sizes, labels=labels, colors=["#EF233C","#eb5e28","#3a0ca3","#36b5ff","#b09ae3","#d68c45","#00bbf9"],autopct='%1.1f%%', startangle=60,textprops={'color':'black','weight':'bold','fontsize':13.5})
ax.axis('equal')
plt.show()

#Scatter Plot for Lowest Prices
fig, axs = plt.subplots(figsize=(15,5))
ax=sns.stripplot(x=df.Month, y=df.Lowest)
plt.title('Scatter Plot for Lowest Prices')
plt.grid()
plt.show(block=False)
plt.pause(5)
plt.close(1)

#Scatter Plot for Highest Prices
fig, axs = plt.subplots(figsize=(15,5))
ax=sns.stripplot(x=df.Month, y=df.Highest)
plt.title('Scatter Plot for Highest Prices')
plt.grid()
plt.show(block=False)
plt.pause(5)
plt.close(1)

#Scatter Plot for Closing Prices
fig, axs = plt.subplots(figsize=(15,5))
ax=sns.stripplot(x=df.Month, y=df.Closing)
plt.title('Scatter Plot for Closing Prices')
plt.grid()
plt.show(block=False)
plt.pause(5)
plt.close(1)

#Line plot of Lowest Prices for each month
plt.rcParams["figure.figsize"] = [16, 6]
for eachMonth in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
    myNewDataFrame = df[df.Month == eachMonth]
#     print(myNewDataFrame)
    yAxis = myNewDataFrame.Lowest
    xAxis = myNewDataFrame.Date
    plt.plot(xAxis, yAxis, marker='.', markerfacecolor="black", markersize=10, color='#C99E10', linewidth=3)
    plt.title(str(eachMonth+"- Lowest Prices"))
    plt.grid()
    plt.xticks(rotation=-45)
    plt.show(block=False)
    plt.pause(5)
    plt.close(1)

#Line plot of Highest Prices for each month
plt.rcParams["figure.figsize"] = [16, 6]
for eachMonth in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
    myNewDataFrame = df[df.Month == eachMonth]
#     print(myNewDataFrame)
    yAxis = myNewDataFrame.Highest
    xAxis = myNewDataFrame.Date
    plt.plot(xAxis, yAxis, marker='.', markerfacecolor="black", markersize=10, color='#C99E10', linewidth=3)
    plt.title(str(eachMonth+"- Highest Prices"))
    plt.grid()
    plt.xticks(rotation=-45)
    plt.show(block=False)
    plt.pause(5)
    plt.close(1)

#Line plot of Lowest Prices for each month
plt.rcParams["figure.figsize"] = [16, 6]
for eachMonth in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
    myNewDataFrame = df[df.Month == eachMonth]
#     print(myNewDataFrame)
    yAxis = myNewDataFrame.Closing
    xAxis = myNewDataFrame.Date
    plt.plot(xAxis, yAxis, marker='.', markerfacecolor="black", markersize=10, color='#C99E10', linewidth=3)
    plt.title(str(eachMonth+"- Closing Prices"))
    plt.grid()
    plt.xticks(rotation=-45)
    plt.show(block=False)
    plt.pause(5)
    plt.close(1)
