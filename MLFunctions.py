#Import all relevant libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from SparQL import run_sparql_query

sparql_results = run_sparql_query()

df_sparql= pd.DataFrame(sparql_results)



def getdata():
    top10 = df_sparql.value_counts().head(10)
    return(top10)
    
def getlowdata():
    low10 = df_sparql.value_counts().tail(10)
    return(low10)

