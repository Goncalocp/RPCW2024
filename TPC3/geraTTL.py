import json

f = open("mapa-virtual.json")
bd = json.load(f)
f.close()

ttl = '''@prefix : <http://rpcw.di.uminho.pt/2024/mapaVirtual/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://rpcw.di.uminho.pt/2024/mapaVirtual/> .

<http://rpcw.di.uminho.pt/2024/mapaVirtual> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/mapaVirtual#destino
:destino rdf:type owl:ObjectProperty ;
         rdfs:domain :Ligacao ;
         rdfs:range :Cidade .


###  http://rpcw.di.uminho.pt/2024/mapaVirtual#origem
:origem rdf:type owl:ObjectProperty ;
        rdfs:domain :Cidade ;
        rdfs:range :Ligacao .


#################################################################
#    Data properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/mapaVirtual#descricao
:descricao rdf:type owl:DatatypeProperty ;
           rdfs:domain :Cidade ;
           rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/mapaVirtual#distancia
:distancia rdf:type owl:DatatypeProperty ;
           rdfs:domain :Ligacao ;
           rdfs:range xsd:float .


###  http://rpcw.di.uminho.pt/2024/mapaVirtual#distrito
:distrito rdf:type owl:DatatypeProperty ;
          rdfs:domain :Cidade ;
          rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/mapaVirtual#nome
:nome rdf:type owl:DatatypeProperty ;
      rdfs:domain :Cidade ;
      rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/mapaVirtual#populacao
:populacao rdf:type owl:DatatypeProperty ;
           rdfs:domain :Cidade ;
           rdfs:range xsd:int .


#################################################################
#    Classes
#################################################################

###  http://rpcw.di.uminho.pt/2024/mapaVirtual#Cidade
:Cidade rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/mapaVirtual#Ligacao
:Ligacao rdf:type owl:Class .


#################################################################
#    Individuals
#################################################################

'''

for cidade in bd["cidades"]:

    ttl += f'''###  http://rpcw.di.uminho.pt/2024/mapaVirtual#{cidade["id"]}
:{cidade["id"]} rdf:type owl:NamedIndividual ,
              :Cidade ;
     :descricao "{cidade["descrição"]}" ;
     :distrito "{cidade["distrito"]}" ;
     :nome "{cidade["nome"]}" ;
     :populacao "{cidade["população"]}"^^xsd:int .

'''

for ligacao in bd["ligacoes"]:

    ttl += f'''###  http://rpcw.di.uminho.pt/2024/mapaVirtual#{ligacao["id"]}
:{ligacao["id"]} rdf:type owl:NamedIndividual ,
              :Ligacao ;
     :destino :{ligacao["destino"]} ;
     :origem :{ligacao["origem"]} ;
     :distancia "{ligacao["distância"]}"^^xsd:float .

'''
    
ttl += "###  Generated by the OWL API (version 4.5.26.2023-07-17T20:34:13Z) https://github.com/owlcs/owlapi"

print(ttl)