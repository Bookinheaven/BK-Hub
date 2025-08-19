import matplotlib.pyplot as plt
import pandas as pd
import os.path as p
import numpy as np

dataset_Path = p.join(p.dirname(p.dirname(__file__)), 'Titanic_visu.csv')

# From csv
if p.isfile(dataset_Path):
    df1 = pd.read_csv(dataset_Path)
    print(df1)

    # Line Plot
    plt.plot([10, 20, 30, 40, 50], [5, 10, 15, 20, 25], linewidth=1, marker='o')
    plt.grid(axis="both", ls="dashdot", lw=1, color='g')
    plt.show()

    # Dot Plot
    plt.plot([10, 20, 30, 40, 50], [5, 10, 15, 20, 25], linewidth=0, marker='o')
    plt.show()

    # Box and whisker plot
    plt.boxplot(df1["Age"])
    plt.show()

    # Scatter Plot
    x = df1["Age"]
    y = df1["Fare"]
    df1.plot.scatter(x='Age', y='Fare')
    df1.plot(kind="scatter", x="Age", y="Fare")    
    plt.scatter(x, y, c=['green'])
    plt.show()

    # Histograms    
    df1["Age"].plot(kind="hist")
    plt.hist(df1["Age"], color='red')
    plt.show()

    # Bar Plot
    counts = [100, 200, 300]
    fuel_type = ("Petrol", 'Diesel', "CNG") 
    index = np.arange(len(fuel_type))
    plt.bar(index, counts, color='red')
    plt.title("Bar Plot")
    plt.ylabel("Fuel Type")
    plt.xlabel("Frequency")
    plt.xticks(index, fuel_type, rotation=90)
    plt.show()

    # Horizontal Bar Plot
    data = df1['Age'].sort_values(axis=0, ascending=False)
    plt.barh([x for x in range(data.size)], data.values)
    plt.show()

    # Comparative Bar Plot
    N = 10
    ind = np.arange(N)
    print("Data: ", ind)
    width=0.36
    x = df1['Fare'].head(10)
    bar1 = plt.bar(ind, x, width, color='r')
    y = df1['New_Fare'].head(10)
    bar2 = plt.bar(ind+width, y, width, color='g')
    plt.show()

    # Stacked Bar Plot
    plt.bar(df1["Age"], df1["Fare"])
    plt.bar(df1["Age"], df1["New_Fare"], bottom=df1["Fare"])
    plt.xlabel("Age")
    plt.ylabel("Fare")
    plt.show()

    # Pie Chart
    data1 = df1["Age"].value_counts()
    plt.pie(data1.values, labels=data1.index, autopct="%1.1f%%")
    plt.show()
