#Import all relevant libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df= pd.read_excel("Dataset_SER531.xlsx")


top10 = df["AREA NAME"].value_counts().head(10)
low10 = df["AREA NAME"].value_counts().tail(10)

def getdata():
    return(top10)
def getlowdata():
    return(low10)

