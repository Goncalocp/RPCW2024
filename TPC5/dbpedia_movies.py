import requests, json

data = {}
filmes = []

sparql_endpoint = "http://dbpedia.org/sparql"

for i in range(2):

    offset = i*10000
    
    sparql_query = f"""
    SELECT DISTINCT ?movie ?title ?director ?writer ?musician ?duration WHERE {{
        ?movie rdf:type <http://dbpedia.org/ontology/Film> .
        optional {{ ?movie rdfs:label ?title .
                    filter(lang(?title)='en') . }}
        optional {{ ?movie dbo:director ?director . }}
        optional {{ ?movie dbo:writer ?writer . }}
        optional {{ ?movie dbo:musicComposer ?musician . }}
        optional {{ ?movie dbo:runtime ?duration . }}
        
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
            filme = {"uri": result["movie"]["value"]}
            if "title" in result:
                filme["nome"] = result["title"]["value"]
            if "director" in result:
                filme["diretor"] = result["director"]["value"]
            if "writer" in result:
                filme["escritor"] = result["writer"]["value"]
            if "musician" in result:
                filme["musico"] = result["musician"]["value"]
            if "duration" in result:
                filme["duracao"] = result["duration"]["value"]
            filmes.append(filme)

    else:
        print("Error:", response.status_code)
        print(response.text)

data['filmes'] = filmes
atores = []

for filme in filmes:

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
f = open("cinema.json","w")
json.dump(data, f, indent=4)
f.close()
