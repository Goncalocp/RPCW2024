import json

f = open("aval-alunos.json")
bd = json.load(f)
f.close()

ttl = '''@prefix : <http://rpcw.di.uminho.pt/2024/alunos/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://rpcw.di.uminho.pt/2024/alunos/> .

<http://rpcw.di.uminho.pt/2024/alunos> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/alunos#temExame
:temExame rdf:type owl:ObjectProperty ;
          rdfs:domain :Aluno ;
          rdfs:range :Exame .


###  http://rpcw.di.uminho.pt/2024/alunos#temTPC
:temTPC rdf:type owl:ObjectProperty ;
        rdfs:domain :Aluno ;
        rdfs:range :TPC .


###  http://www.w3.org/2002/07/owl#topObjectProperty
owl:topObjectProperty rdfs:domain :Aluno ;
                      rdfs:range :Exame .


#################################################################
#    Data properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/alunos#curso
:curso rdf:type owl:DatatypeProperty ;
       rdfs:domain :Aluno ;
       rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/alunos#epocaExame
:epocaExame rdf:type owl:DatatypeProperty ;
            rdfs:domain :Exame ;
            rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/alunos#id
:id rdf:type owl:DatatypeProperty ;
    rdfs:domain :Aluno ;
    rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/alunos#nome
:nome rdf:type owl:DatatypeProperty ;
      rdfs:domain :Aluno ;
      rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/alunos#notaExame
:notaExame rdf:type owl:DatatypeProperty ;
           rdfs:domain :Exame ;
           rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/alunos#notaTPC
:notaTPC rdf:type owl:DatatypeProperty ;
         rdfs:domain :TPC ;
         rdfs:range xsd:float .


###  http://rpcw.di.uminho.pt/2024/alunos#projeto
:projeto rdf:type owl:DatatypeProperty ;
         rdfs:domain :Aluno ;
         rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/alunos#tp
:tp rdf:type owl:DatatypeProperty ;
    rdfs:domain :TPC ;
    rdfs:range xsd:string .


#################################################################
#    Classes
#################################################################

###  http://rpcw.di.uminho.pt/2024/alunos#Aluno
:Aluno rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/alunos#Exame
:Exame rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/alunos#TPC
:TPC rdf:type owl:Class .


#################################################################
#    Individuals
#################################################################
'''

for aluno in bd['alunos']:
    registo = f'''
###  http://rpcw.di.uminho.pt/2024/alunos#{aluno['idAluno']}
:{aluno['idAluno']} rdf:type owl:NamedIndividual ,
                  :Aluno ;
                          :curso "{aluno['curso']}" ;
                          :id "{aluno['idAluno']}" ;
                          :nome "{aluno['nome']}" ;
                          :projeto "{aluno['projeto']}"^^xsd:int ;
                          :temExame'''

    for exame in list(aluno['exames'].keys()):
        registo += f''' :{aluno['idAluno']}_{exame} ,
                                   '''
    registo = registo[:-37] + ';'
    registo += '''
                          :temTPC '''
    for tpc in aluno['tpc']:
        registo += f''' :{aluno['idAluno']}_{tpc['tp']} ,                                  
                                  '''
    
    registo = registo[:-70] + '.'
    
    for exame, nota in aluno['exames'].items():
        registo += f'''

###  http://rpcw.di.uminho.pt/2024/alunos#{aluno['idAluno']}_{exame} 
:{aluno['idAluno']}_{exame} rdf:type owl:NamedIndividual ,
                           :Exame ;
        :epocaExame "{exame}" ;
        :notaExame {nota} .'''
    
    for tpc in aluno['tpc']:
        registo += f'''
###  http://rpcw.di.uminho.pt/2024/alunos#{aluno['idAluno']}_{tpc['tp']}
:{aluno['idAluno']}_{tpc['tp']} rdf:type owl:NamedIndividual ,
                       :TPC ;
      :notaTPC "{tpc['nota']}"^^xsd:float ;
      :tp "{tpc['tp']}" .
'''

    ttl += registo

print(ttl)