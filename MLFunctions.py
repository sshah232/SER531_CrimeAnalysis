#Import all relevant libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from SparQL import run_sparql_query1




def getdata():
    sparql_results = run_sparql_query1()
    df_sparql = pd.DataFrame(sparql_results)
    top10 = df_sparql.value_counts().head(10)
    # Convert the index to tuple for hashability
    top10.index = top10.index.map(tuple)
    return top10
    
def getlowdata():
    sparql_results = run_sparql_query1()
    df_sparql = pd.DataFrame(sparql_results)
    low10 = df_sparql.value_counts().tail(10)
    # Convert the index to tuple for hashability
    low10.index = low10.index.map(tuple)
    return low10

