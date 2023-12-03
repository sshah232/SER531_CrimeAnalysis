#Import all relevant libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# from mlxtend.frequent_patterns import apriori
# from mlxtend.frequent_patterns import association_rules


    #Load the file into pandas

df2= pd.read_excel("Dataset_SER531.xlsx")
    #check first 5 rows



    #Drop all rows with a null value

df2.dropna(inplace=True)


top15 = df2["AREA NAME"].value_counts().head(10)
low10 = df2["AREA NAME"].value_counts().tail(10)
def getdata():
    return(top15)
def getlowdata():
    return(low10)

