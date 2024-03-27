from flask import Flask, render_template, url_for
from datetime import datetime
import requests

app = Flask(__name__)

# data do sistema no formato ISO
data_hora_atual = datetime.now()
data_iso_formatada = data_hora_atual.strftime('%Y-%m-%dT%H:%M:%S')

# Graphdb endpoint
graphdb_endpoint = "http://epl.di.uminho.pt:7200/repositories/cinema2024"

@app.route('/')
def index():
    return render_template('index.html', data = {'data': data_iso_formatada})

@app.route('/filmes')
def filmes():
    sparql_query = '''
prefix : <http://rpcw.di.uminho.pt/2024/cinema/>

select ?film ?title ?abstract where {
    ?film a :Film ;
          :title ?title .
    optional {{?film :abstract ?abstract}}
} order by ?title
'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('filmes.html', data = {'data': data_iso_formatada, 'dados': dados})
    else:
        return render_template('empty.html')
    
@app.route('/pessoas')
def pessoas():
    sparql_query = '''
prefix : <http://rpcw.di.uminho.pt/2024/cinema/>

select ?person ?name where {
    ?person a :Person ;
            :name ?name .
} order by ?person
'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('pessoas.html', data = {'data': data_iso_formatada, 'dados': dados})
    else:
        return render_template('empty.html')


@app.route('/pessoas/<nome>')
def pessoa(nome):
    sparql_query = f'''
prefix : <http://rpcw.di.uminho.pt/2024/cinema/>
select ?person ?name ?bdate ?film ?title where {{
    ?person a :Person ; 
            :name ?name ;
    optional {{?person :birthDate ?bdate  }}        
    optional {{ ?film :hasActor ?person ; 
                      :title ?title .
             }}
    optional {{ ?film :hasComposer ?person ; 
                      :title ?title .
             }}
    optional {{ ?film :hasDirector ?person ; 
                      :title ?title .
             }}
    optional {{ ?film :hasProducer ?person ; 
                      :title ?title .
             }}
    optional {{ ?film :hasWriter ?person ; 
                      :title ?title .
             }}
    filter(str(?person) = "http://rpcw.di.uminho.pt/2024/cinema/{nome}")
}} order by ?film
'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('pessoa.html', data = {'data': data_iso_formatada, 'dados': dados})
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })

@app.route('/filmes/<nome>')
def filme(nome):
    sparql_query = f'''
prefix : <http://rpcw.di.uminho.pt/2024/cinema/>

select ?film ?title ?abstract ?duration ?genre ?date ?country ?actor ?producer ?director ?composer ?writer where {{
    ?film a :Film ;
          :title ?title .
    optional {{ ?film :description ?abstract . }}
    optional {{ ?film :duration ?duration . }}
    optional {{ ?film :hasGenre ?genre . }}
    optional {{ ?film :releaseDate ?date . }}
    optional {{ ?film :hasCountry ?country . }}
    optional {{ ?film :hasActor ?actor . }}
    optional {{ ?film :hasProducer ?producer . }}
    optional {{ ?film :hasDirector ?director . }}
    optional {{ ?film :hasComposer ?composer . }}
    optional {{ ?film :hasWriter ?writer . }}
    
    filter(str(?film) = "http://rpcw.di.uminho.pt/2024/cinema/{nome}")
}}
'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        
        abstract = []
        durations = []
        genres = []
        dates = []
        countries = []
        cast = []
        producers = []
        directors = []
        composers = []
        writers = []
        
        for entry in dados:
            if 'abstract' in entry.keys():
                if entry['abstract']['value'] not in abstract:
                    abstract.append(entry['abstract']['value'])
            if 'duration' in entry.keys():
                if entry['duration']['value'] not in durations:
                    durations.append(entry['duration']['value'])
            if 'genre' in entry.keys():
                if entry['genre']['value'].split('/')[-1] not in genres:
                    genres.append(entry['genre']['value'].split('/')[-1])
            if 'date' in entry.keys():
                if entry['date']['value'] not in dates:
                    dates.append(entry['date']['value'])                    
            if 'country' in entry.keys():
                if entry['country']['value'].split('/')[-1] not in countries:
                    countries.append(entry['country']['value'].split('/')[-1])
            if 'actor' in entry.keys():
                if entry['actor']['value'] not in cast:
                    cast.append(entry['actor']['value'])
            if 'producer' in entry.keys():
                if entry['producer']['value'] not in producers:
                    producers.append(entry['producer']['value'])
            if 'director' in entry.keys():
                if entry['director']['value'] not in directors:
                    directors.append(entry['director']['value'])
            if 'composer' in entry.keys():
                if entry['composer']['value'] not in composers:
                    composers.append(entry['composer']['value'])
            if 'writer' in entry.keys():
                if entry['writer']['value'] not in writers:
                    writers.append(entry['writer']['value'])

        dados = {
            'film': filme,
            'title': dados[0]['title']['value'],
            'abstract': abstract,
            'durations': durations,
            'genres': genres,
            'dates': dates,
            'countries': countries,
            'cast': cast,
            'producers': producers,
            'directors': directors,
            'composers': composers,
            'writers': writers
        }


        return render_template('filme.html', data = {'data': data_iso_formatada, 'dados': dados})
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })

if __name__ == '__main__':
    app.run(debug=True)