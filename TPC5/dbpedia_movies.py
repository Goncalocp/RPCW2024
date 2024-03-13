import requests, json

data = {}
filmes = []

sparql_endpoint = "http://dbpedia.org/sparql"

for i in range(18):

    offset = i*10000
    
    sparql_query = f"""
    SELECT DISTINCT ?movie ?title ?director ?writer ?musician ?duration WHERE {{
        ?movie rdf:type <http://dbpedia.org/ontology/Film> ;
                       rdfs:label ?title ;
                       dbo:director ?director ;
                       dbo:writer ?writer ;
                       dbo:musicComposer ?musician ;
                       dbo:runtime ?duration
        filter(lang(?title)='en') .
    }} limit 2 offset {offset}
    """
    

    headers = {
        "Accept": "application/sparql-results+json"
    }

    params = {
        "query": sparql_query,
        "format": "json"
    }

    response = requests.get(sparql_endpoint, params=params, headers=headers)

    if response.status_code == 200:
        results = response.json()

        for result in results["results"]["bindings"]:
            filmes.append({
                "uri": result["movie"]["value"],
                "nome": result["title"]["value"],
                "diretor": result["director"]["value"],
                "escritor": result["writer"]["value"],
                "musico": result["musician"]["value"],
                "duracao": result["duration"]["value"]
            })

    else:
        print("Error:", response.status_code)
        print(response.text)

data['filmes'] = filmes
atores = []

for filme in filmes:

    print(filme['nome'])

    sparql_query = f"""
    SELECT DISTINCT ?actor ?name ?abstract WHERE {{
        <{filme['uri']}> dbo:starring ?actor .
        optional {{?actor rdfs:label ?name .
                   filter(lang(?name)='en') . }}
        optional {{?actor dbo:abstract ?abstract .
                   filter(lang(?abstract)='en') . }}
    }}
    """
    
    headers = {
    "Accept": "application/sparql-results+json"
    }

    params = {
        "query": sparql_query,
        "format": "json"
    }

    response = requests.get(sparql_endpoint, params=params, headers=headers)

    if response.status_code == 200:
        results = response.json()
        filme['elenco'] = []

        for result in results["results"]["bindings"]:
            
            ator = {}
            ator['uri'] = result['actor']['value']
            if 'name' in result.keys():
                ator['nome'] = result['name']['value']
            if 'abstract' in result.keys():
                ator['resumo'] = result['abstract']['value']

            filme['elenco'].append(ator['uri'])
            atores.append(ator)

    else:
        print("Error:", response.status_code)
        print(response.text)

data['atores'] = atores
f = open("filmes.json","w")
json.dump(data, f, indent=4)
f.close()