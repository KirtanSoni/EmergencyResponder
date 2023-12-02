from rdflib import Graph, Namespace

def owlquery(owl_file_path,zip,state,city):
    """
    Returns an RDFLib Graph object containing the ontology.
    """
    return "incomplete"
    # g = Graph()
    # g.parse(owl_file_path)

    # location = Namespace("https://dbpedia.org/ontology/location#")

    # results = g.query(query, initNs={'location': location})
    # for row in results:
    #     city_uri = row.city
    #     city_name = city_uri.split("#")[-1]
    #     print(city_name)