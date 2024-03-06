from flask import Flask, render_template, url_for
from datetime import datetime
import requests

app = Flask(__name__)

# data do sistema no formato ISO
data_hora_atual = datetime.now()
data_iso_formatada = data_hora_atual.strftime('%Y-%m-%dT%H:%M:%S')

# Graphdb endpoint
graphdb_endpoint = "http://localhost:7200/repositories/tabelaPeriodica"

@app.route('/')
def index():
    return render_template('index.html', data = {'data': data_iso_formatada})

@app.route('/elementos')
def elementos():
    sparql_query = '''
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
select ?nome ?simb ?na ?grupo where {
    ?s a tp:Element ;
       tp:name ?nome ;
       tp:symbol ?simb ;
       tp:atomicNumber ?na ;
       tp:group ?grupo .
} order by ?nome
'''
    resposta = requests.get(graphdb_endpoint,
                            params= {"query": sparql_query}, 
                            headers= {'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('elementos.html', data = {'data': data_iso_formatada, 'dados': dados})
    else:
        return render_template('empty.html', data = data_iso_formatada)

@app.route('/elemento/<nome>')
def elemento(nome):
    sparql_query = f'''
PREFIX tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
SELECT ?nome ?grupo ?simb ?num ?aw ?b ?cr ?c ?col ?period ?ss WHERE {{
    ?s a tp:Element ;
       tp:name "{nome}" ;
       tp:group ?grupo ;
       tp:symbol ?simb ;
       tp:atomicNumber ?num .
    optional {{ ?s tp:atomicWeight ?aw . }}
    optional {{ ?s tp:block ?b . }}
    optional {{ ?s tp:casRegistryID ?cr . }}
    optional {{ ?s tp:classification ?c . }}
    optional {{ ?s tp:color ?col . }}
    optional {{ ?s tp:period ?period . }}
    optional {{ ?s tp:standardState ?ss .}}
}}
'''
    resposta = requests.get(graphdb_endpoint,
                            params= {"query": sparql_query}, 
                            headers= {'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('elemento.html', data = {'data': data_iso_formatada, 'dados': dados, 'nome': nome})
    else:
        return render_template('empty.html', data = data_iso_formatada)

@app.route('/grupos')
def grupos():
    sparql_query = '''
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
SELECT ?grupo (COUNT(?el) as ?numElem) WHERE { 
    ?grupo rdf:type tp:Group .
    ?el tp:group ?grupo .
} GROUP BY (?grupo)
ORDER BY (?numElem)
'''
    resposta = requests.get(graphdb_endpoint,
                            params= {"query": sparql_query}, 
                            headers= {'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('grupos.html', data = {'data': data_iso_formatada, 'dados': dados})
    else:
        return render_template('empty.html', data = data_iso_formatada)
    
@app.route('/grupos/<nome>')
def grupo(nome):
    sparql_query = f'''
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
select ?nome ?num ?elnome where {{
  ?group a tp:Group .
    optional {{ ?group tp:name ?nome . }}
    optional {{ ?group tp:number ?num . }}
    ?group tp:element ?elem .
    ?elem tp:name ?elnome .
    filter(str(?group) = "http://www.daml.org/2003/01/periodictable/PeriodicTable#{nome}")
}}
'''
    resposta = requests.get(graphdb_endpoint,
                            params= {"query": sparql_query}, 
                            headers= {'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('grupo.html', data = {'data': data_iso_formatada, 'dados': dados})
    else:
        return render_template('empty.html', data = data_iso_formatada)


if __name__ == '__main__':
    app.run(debug=True)