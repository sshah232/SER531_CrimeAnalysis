from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd





def run_sparql_query1():
    sparql = SPARQLWrapper("http://ec2-18-216-173-36.us-east-2.compute.amazonaws.com:3030/New_DS/query")
    sparql.setReturnFormat(JSON)

    sparql.setQuery("""
PREFIX crime: <http://www.semanticweb.org/yugmapatel/ontologies/2023/10/CrimeDataOntology#>
PREFIX DUL: <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#>
PREFIX :	<http://www.semanticweb.org/yugmapatel/ontologies/2023/10/CrimeDataOntology/>
SELECT  ?Area (COUNT(?sub) AS ?crimeCount)
WHERE {
   ?sub :hasAddress ?Area .

}
GROUP BY ?Area
ORDER BY DESC(?sub)
LIMIT 10
    """)

    try:
        ret = sparql.queryAndConvert()
        df_results = pd.DataFrame(ret)
        return df_results
    except Exception as e:
        print(e)
        return None



def run_sparql_query2():
    sparql = SPARQLWrapper("http://ec2-18-216-173-36.us-east-2.compute.amazonaws.com:3030/New_DS/query")
    sparql.setReturnFormat(JSON)

    sparql.setQuery("""
PREFIX crime: <http://www.semanticweb.org/yugmapatel/ontologies/2023/10/CrimeDataOntology#>
PREFIX DUL: <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#>
PREFIX :	<http://www.semanticweb.org/yugmapatel/ontologies/2023/10/CrimeDataOntology/>
SELECT  ?Area (COUNT(?sub) AS ?crimeCount)
WHERE {
   ?sub :hasAddress ?Area .

}
GROUP BY ?Area
ORDER BY ASC(?sub)
LIMIT 10
    """)

    try:
        ret = sparql.queryAndConvert()
        df_results = pd.DataFrame(ret)
        return df_results
    except Exception as e:
        print(e)
        return None


def run_sparql_query3():
    sparql = SPARQLWrapper("http://ec2-18-216-173-36.us-east-2.compute.amazonaws.com:3030/New_DS/query")
    sparql.setReturnFormat(JSON)

    sparql.setQuery("""
PREFIX crime: <http://www.semanticweb.org/yugmapatel/ontologies/2023/10/CrimeDataOntology#>
PREFIX DUL: <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#>
PREFIX :	<http://www.semanticweb.org/yugmapatel/ontologies/2023/10/CrimeDataOntology/>
SELECT  *
WHERE {
   ?sub :hasGender ?Gender .
  ?sub :hasCrimeDescription ?Description
 FILTER (?Gender = "M")
}
    """)

    try:
        ret = sparql.queryAndConvert()
        df_results = pd.DataFrame(ret)
        return df_results
    except Exception as e:
        print(e)
        return None
       
