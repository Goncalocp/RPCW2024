import json

f = open("plantas.json")
bd = json.load(f)
f.close()

ttl = '''@prefix : <http://rpcw.di.uminho.pt/2024/plantas/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://rpcw.di.uminho.pt/2024/plantas/> .

<http://rpcw.di.uminho.pt/2024/plantas> rdf:type owl:Ontology .

#################################################################
#    Annotation properties
#################################################################

###  http://purl.org/dc/elements/1.1/creator
<http://purl.org/dc/elements/1.1/creator> rdf:type owl:AnnotationProperty .


#################################################################
#    Object Properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/plantas#atualizadoEm
:atualizadoEm rdf:type owl:ObjectProperty ;
              rdfs:domain :Planta ;
              rdfs:range :DataAtualização ;
              <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#daEspecie
:daEspecie rdf:type owl:ObjectProperty ;
           rdfs:domain :Planta ;
           rdfs:range :Espécie ;
           <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#doGestor
:doGestor rdf:type owl:ObjectProperty ;
          rdfs:domain :Planta ;
          rdfs:range :Gestor ;
          <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#intervencionada
:intervencionada rdf:type owl:ObjectProperty ;
                 rdfs:domain :Planta ;
                 rdfs:range :NúmeroIntervenções ;
                 <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#naData
:naData rdf:type owl:ObjectProperty ;
        rdfs:domain :Planta ;
        rdfs:range :DataPlantação ;
        <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#naImplantacao
:naImplantacao rdf:type owl:ObjectProperty ;
               rdfs:domain :Planta ;
               rdfs:range :Implantação ;
               <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#noEstado
:noEstado rdf:type owl:ObjectProperty ;
          rdfs:domain :Planta ;
          rdfs:range :Estado ;
          <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#onde
:onde rdf:type owl:ObjectProperty ;
      rdfs:domain :Planta ;
      rdfs:range :CódigoRua ;
      <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#temCaldeira
:temCaldeira rdf:type owl:ObjectProperty ;
             rdfs:domain :Planta ;
             rdfs:range :Caldeira ;
             <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#temOrigem
:temOrigem rdf:type owl:ObjectProperty ;
           rdfs:domain :Planta ;
           rdfs:range :Origem ;
           <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#temTutor
:temTutor rdf:type owl:ObjectProperty ;
          rdfs:domain :Planta ;
          rdfs:range :Tutor ;
          <http://purl.org/dc/elements/1.1/creator> "goncalo" .


#################################################################
#    Data properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/plantas#freguesia
:freguesia rdf:type owl:DatatypeProperty ;
           rdfs:domain :CódigoRua ;
           rdfs:range xsd:string ;
           <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#id
:id rdf:type owl:DatatypeProperty ;
    rdfs:domain :Planta ;
    rdfs:range xsd:int ;
    <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#local
:local rdf:type owl:DatatypeProperty ;
       rdfs:domain :CódigoRua ;
       rdfs:range xsd:string ;
       <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#nomeCientifico
:nomeCientifico rdf:type owl:DatatypeProperty ;
                rdfs:domain :Espécie ;
                rdfs:range xsd:string ;
                <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#número
:número rdf:type owl:DatatypeProperty ;
        rdfs:domain :Planta ;
        rdfs:range xsd:int ;
        <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#rua
:rua rdf:type owl:DatatypeProperty ;
     rdfs:domain :CódigoRua ;
     rdfs:range xsd:string ;
     <http://purl.org/dc/elements/1.1/creator> "goncalo" .


#################################################################
#    Classes
#################################################################

###  http://rpcw.di.uminho.pt/2024/plantas#Caldeira
:Caldeira rdf:type owl:Class ;
          <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#CódigoRua
:CódigoRua rdf:type owl:Class ;
           <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#DataAtualização
:DataAtualização rdf:type owl:Class ;
                 <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#DataPlantação
:DataPlantação rdf:type owl:Class ;
               <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#Espécie
:Espécie rdf:type owl:Class ;
         <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#Estado
:Estado rdf:type owl:Class ;
        <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#Gestor
:Gestor rdf:type owl:Class ;
        <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#Implantação
:Implantação rdf:type owl:Class ;
             <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#NúmeroIntervenções
:NúmeroIntervenções rdf:type owl:Class ;
                    <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#Origem
:Origem rdf:type owl:Class ;
        <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#Planta
:Planta rdf:type owl:Class ;
        <http://purl.org/dc/elements/1.1/creator> "goncalo" .


###  http://rpcw.di.uminho.pt/2024/plantas#Tutor
:Tutor rdf:type owl:Class ;
       <http://purl.org/dc/elements/1.1/creator> "goncalo" .


#################################################################
#    Individuals
#################################################################

'''

for planta in bd:
    
    if '/' in str(planta["Número de intervenções"]):
        planta["Número de intervenções"] = 0
        
    registo = f'''
###  http://rpcw.di.uminho.pt/2024/plantas#{planta["Estado"]}
:{planta["Estado"]} rdf:type owl:NamedIndividual ,
                 :Estado .


###  http://rpcw.di.uminho.pt/2024/plantas#{planta["Implantação"].replace(" ","_")}
:{planta["Implantação"].replace(" ","_")} rdf:type owl:NamedIndividual ,
                     :Implantação .


###  http://rpcw.di.uminho.pt/2024/plantas#{planta["Gestor"].replace(" ","_")}
:{planta["Gestor"].replace(" ","_")} rdf:type owl:NamedIndividual ,
               :Gestor .


###  http://rpcw.di.uminho.pt/2024/plantas#{planta["Caldeira"]}
:{planta["Caldeira"]} rdf:type owl:NamedIndividual ,
              :Caldeira .


###  http://rpcw.di.uminho.pt/2024/plantas#{planta["Origem"].replace(" ","_")}
:{planta["Origem"].replace(" ","_")} rdf:type owl:NamedIndividual ,
            :Origem .


###  http://rpcw.di.uminho.pt/2024/plantas#{planta["Espécie"].replace(" ","_")}
:{planta["Espécie"].replace(" ","_")} rdf:type owl:NamedIndividual ,
                         :Espécie .


###  http://rpcw.di.uminho.pt/2024/plantas#{planta["Tutor"]}
:{planta["Tutor"]} rdf:type owl:NamedIndividual ,
              :Tutor .


###  http://rpcw.di.uminho.pt/2024/plantas#{planta["Data de Plantação"].replace("/","_")}
:{planta["Data de Plantação"].replace("/","_")} rdf:type owl:NamedIndividual ,
            :DataPlantação .


###  http://rpcw.di.uminho.pt/2024/plantas#{planta["Código de rua"]}
<http://rpcw.di.uminho.pt/2024/plantas#{planta["Código de rua"]}> rdf:type owl:NamedIndividual ,
                                                         :CódigoRua .


###  http://rpcw.di.uminho.pt/2024/plantas#{planta["Data de actualização"].replace(" ","_")}
<http://rpcw.di.uminho.pt/2024/plantas#{planta["Data de actualização"].replace(" ","_")}> rdf:type owl:NamedIndividual ,
                                                                     :DataAtualização .


###  http://rpcw.di.uminho.pt/2024/plantas#{planta["Número de Registo"]}
<http://rpcw.di.uminho.pt/2024/plantas#{planta["Número de Registo"]}> rdf:type owl:NamedIndividual ,
                                                   :Planta ;
                                          :atualizadoEm <http://rpcw.di.uminho.pt/2024/plantas#{planta["Data de actualização"].replace(" ","_")}> ;
                                          :daEspecie :{planta["Espécie"].replace(" ","_")} ;
                                          :doGestor :{planta["Gestor"].replace(" ","_")} ;
                                          :intervencionada <http://rpcw.di.uminho.pt/2024/plantas#{planta["Número de intervenções"]}> ;
                                          :naData :{planta["Data de Plantação"].replace("/","_")} ;
                                          :naImplantacao :{planta["Implantação"].replace(" ","_")} ;
                                          :noEstado :{planta["Estado"]} ;
                                          :temCaldeira :{planta["Caldeira"]} ;
                                          :temOrigem :{planta["Origem"].replace(" ","_")} ;
                                          :temTutor :{planta["Tutor"]} ;
                                          :freguesia "{planta["Freguesia"]}" ;
                                          :id "{planta["Id"]}"^^xsd:int ;
                                          :local "{planta["Local"]}" ;
                                          :nomeCientifico "{planta["Nome Científico"]}" ;
                                          :número "{planta["Número de Registo"]}"^^xsd:int .


###  http://rpcw.di.uminho.pt/2024/plantas#{planta["Número de intervenções"]}
<http://rpcw.di.uminho.pt/2024/plantas#{planta["Número de intervenções"]}> rdf:type owl:NamedIndividual ,
                                                   :NúmeroIntervenções .
'''
    ttl += registo

ttl += '''

###  Generated by the OWL API (version 4.5.26.2023-07-17T20:34:13Z) https://github.com/owlcs/owlapi'''

print(ttl)