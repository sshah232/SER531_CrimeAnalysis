from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd

def run_sparql_query():
    sparql = SPARQLWrapper("http://ec2-18-216-173-36.us-east-2.compute.amazonaws.com:3030/#/dataset/New_DS/")
    sparql.setReturnFormat(JSON)

    sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT * WHERE {
            ?sub ?pred ?obj .
        } LIMIT 10
    """)

    try:
        ret = sparql.queryAndConvert()
        results = [r for r in ret["results"]["bindings"]]
        df_results = pd.DataFrame(results)
        return df_results
    except Exception as e:
        print(e)
        return None