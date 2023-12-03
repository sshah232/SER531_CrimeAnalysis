from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://ec2-18-223-133-72.us-east-2.compute.amazonaws.com:3030/New_DS/query")
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

    for r in ret["results"]["bindings"]:
        print(r)
except Exception as e:
    print(e)
