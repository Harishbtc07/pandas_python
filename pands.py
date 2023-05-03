#Pandas

import pandas as pd


data=pd.read_csv("C:\\Users\\Harish Reddy\\Downloads\\StatewiseTestingDetails.csv")
df=pd.DataFrame(data)
print(df)

#Printing first five rows of data frame
print(df.head())

##Printing first two rows of data frame
print(df.head(2))

#Printing last five rows of data frame
print(df.tail())

#Printing last two rows of data frame
print(df.tail(2))

# describe() method returns description of the data in the DataFrame
print(df.describe())

#shape attribute in Pandas enables us to obtain the shape of a DataFrame
print(df.shape)

print(df[0:10:2])

print(df['TotalSamples'])

print(df[['Negative','Positive']])

print(df[['State','Negative','Positive']])

print(df[['State','Negative','Positive']][0:10:2])

# for rec in df.iterrows():
#     print(rec)


#LOC

print(df.loc[4])

print(df.loc[4,['State']])

print(df.loc[0:6])

print(df.loc[0:6,['State','Positive']])

print(df.loc[0:5,'State':'TotalSamples'])

#ILOC

print(df.iloc[0:5])

print(df.iloc[1,4])

print(df.iloc[0:4,0:2])

print(df.iloc[0:4,2])

print(df.iloc[[1,2,4,5]])

print(df.iloc[:,[2,4]])

print(df.iloc[0:4,[1,4]])

#Sortingthe dataframe

print(df.sort_values('Positive'))

print(df.sort_values('Positive',ascending=False))

print(df.sort_values(['Negative','Positive']))

#Manupulating data frame

#we can add,delete and modify the coloumns
df['Total']=0
print(df)

#Deleting coloumn
df['Perc']='pass/fail'
print(df)

print(df.drop(columns='Perc'))

print(df)

print(df.drop(columns='Perc',inplace=True))

print(df)

#Removing Duplicates
#knowing Duplicates
print(df.duplicated())

#Removing Duplicates
print(df.drop_duplicates())

#Handling missing data

#Filling with default value
print(df.fillna(1200))

print(df['Negative'].fillna(1200))

#Droping Missing Data
print(df.dropna())

print(df)

df.dropna(inplace=True)

print(df)

#Data Filtering and coditional changes

print(df.loc[df['Positive']>50000])


print(df.loc[df['State'].str.contains('a')])

print(df.loc[df['State'].str.startswith('H')])

print(df.loc[df['State'].str.endswith('d')])

