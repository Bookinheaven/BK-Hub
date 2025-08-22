import pandas as pd
import os.path as p
import numpy as np

dataset_Path = p.join(p.dirname(p.dirname(__file__)), 'Titanic_visu.csv')

# From list
data1 = np.array([3,5,77])
df2 = pd.DataFrame(data1)
print(df2)

# From list of list
data2 = np.array([[3,5,77], [4,32,11]])
df3 = pd.DataFrame(data2)
print(df3)

# Column names and index
df4 = pd.DataFrame([["Hary", 21], ["John", 13]], columns = ['Name','Age'], index=["name 1", "name 2"])
print(df4)

# From Dictionary
data3 = { 'Name' : ['John', 'James', 'Jerry']}
df5 = pd.DataFrame(data3)
print(df5) 

# From List using Dictionary
data4 = {
    'Name' : ['John','James','Jerry'],
    'Age' : [50,35,27]
}
df6 = pd.DataFrame(data4)
print(df6) 

# From csv
if p.isfile(dataset_Path):

    # Data Selection
    df1 = pd.read_csv(dataset_Path, na_values="#", usecols=['Name', 'Age'])
    print(df1)
    print(df1['Age'].head())
    print(df1.Age.head())
    print(df1.head(10))
    print(df1.tail(10))
    print(df1.index)
    print(df1.columns)
    print(df1.values)
    
    # Data Description 
    print(df1.shape)
    print(df1.describe())
    print(df1.describe(include="all")) # all, object
    print(df1.value_counts())
    print(df1.info())
    print(df1.size)
    print(df1.ndim)
    print(df1.dtypes) 
    
    # Data Filtering
    print(df1.isnull())
    print(df1.isnull().sum()) # total no of nulls in each column
    print(df1.isnull().sum().sum()) # total no of nulls in complete data

    # Data Manipulation 
    df1 = pd.read_csv(dataset_Path)
    print(df1.max())
    print(df1.count())
    print(df1.sum())
    print(df1.min())
    print(df1.max())
    print(df1['Concession'].apply(np.sqrt))
    df1['New Column'] = df1['Age'] + 10
    print(df1['New Column'])
    
    # Delete row
    df1 = df1.drop(df1.index[-1])

    # Add row
    new_row = {'Name':'Test','Age':40,'Sex':'male','Fare':200,'Pclass':1}
    df1 = pd.concat([df1, pd.DataFrame([new_row])], ignore_index=True)
    print(df1.tail(2))

    # Impute Missing Values
    df1['Survived'] = df1['Survived'].fillna(df1['Survived'].median())   # Fill with median
    df1['Embarked'] = df1['Embarked'].fillna('Unknown') # Fill with string
    df1.dropna(axis=1) # Deleting the columns with missing data
    df1.dropna(axis=0) # Deleting the rows with missing data
    df1.dropna(how='any', subset=['Age']) # Deleting the rows for a specific column with missing data
    """ 
        how = 'any': at least one value must be null.
        how = 'all': all values must be null.
    """
    # Replacing with the value from the previous row or the next row
    df1 = df1.fillna(method='ffill') # or df1.ffill(axis=?) 
    df1 = df1.fillna(method='bfill') # or df1.bfill(axis=?)  
    
    # Interpolate
    df_inter = df1.interpolate(method="linear")
    """
        method='polynomial', order=2 → Fits a polynomial curve.
        method='time' → For datetime indexes.
        method='pad' or method='ffill' → Forward fill.
        method='bfill' → Backward fill.
    """
    
                                            
    # Slicing the Dataset
    print(df1['Age'].head()) # (a) Based on single column
    print(df1[['Age','Sex','Fare']].head()) # (b) Based on multiple columns

    print(df1.iloc[5])   # 6th row [(c) Based on single row]
    print(df1.iloc[5:8])   # Rows 5 to 7 [(d) Based on multiple rows]

    print(df1.loc[0:5, ['Sex','Age']])  # Rows 0–5, columns sex & age

    # Conditional slicing
    print(df1[df1['Age'] > 30]) # Passengers older than 30
    print(df1[(df1['Age'] > 30) & (df1['Sex'] == 'male')]) # Males older than 30
    
    # GroupBy and Aggregation
    print(df1.groupby('Sex')['Age'].mean()) # Mean Age by Sex
    print(df1.groupby(['Sex','Pclass'])['Fare'].mean())

    # Sorting
    print(df1.sort_values('Age').head()) # By one column
    print(df1.sort_values(['Pclass','Age']).head()) # By multiple cols

    # Ranking
    df1['fare_rank'] = df1['Fare'].rank()
    print(df1[['Fare','fare_rank']].head())

    # Pivot Table
    pivot = df1.pivot_table(values='Fare', index='Sex', columns='Pclass', aggfunc='mean')
    print(pivot)
