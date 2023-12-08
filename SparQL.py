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
        # print(ret)
        crime_count_dict = {}

        for item in ret['results']['bindings']:
            area = item['Area']['value']
            crime_count = int(item['crimeCount']['value'])
            crime_count_dict[area] = crime_count
        print(crime_count_dict)
        df = pd.DataFrame(list(crime_count_dict.items()), columns=['Area', 'crimeCount'])
        # results = [r for r in ret["results"]["bindings"]]
        # df_results = pd.DataFrame(results)
        return df
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
SELECT  *
WHERE {
   ?sub :hasGender ?Gender .
  ?sub :hasCrimeDescription ?Description
 FILTER (?Gender = "M")
}
LIMIT 20
    """)

    try:
        ret = sparql.queryAndConvert()
        crime_count_dict = {}

        for item in ret['results']['bindings']:
            gender = item['Gender']['value']
            description = item['Description']['value']
            # Assuming 'sub' is not needed in the DataFrame, you can skip it
            key = (gender, description)
            crime_count_dict[key] = crime_count_dict.get(key, 0) + 1

        # Create a DataFrame from the dictionary
        df = pd.DataFrame(list(crime_count_dict.items()), columns=['Gender', 'Description'])
        df[['Gender', 'Description']] = pd.DataFrame(df['Gender'].tolist(), index=df.index)
        df = df[['Gender', 'Description']]
        return df
    except Exception as e:
        print(e)
        return None
    
print(run_sparql_query1())
print(run_sparql_query2())