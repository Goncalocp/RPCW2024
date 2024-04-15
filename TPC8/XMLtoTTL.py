import xml.etree.ElementTree as ET

tree = ET.parse('royal.xml')
root = tree.getroot()

sex = {}

sexProp = {
    'M': 'temPai',
    'F': 'temMae'
}

for person in root.findall("person"):
    if person.find('sex') != None :
        sex[person.find('id').text] = person.find('sex').text
    else:
        sex[person.find('id').text] = None


ttl = '''@prefix : <http://rpcw.di.uminho.pt/2024/familia/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://rpcw.di.uminho.pt/2024/familia/> .

<http://rpcw.di.uminho.pt/2024/familia> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/familia/temMae
:temMae rdf:type owl:ObjectProperty ;
        rdfs:domain :Pessoa ;
        rdfs:range :Pessoa .


###  http://rpcw.di.uminho.pt/2024/familia/temPai
:temPai rdf:type owl:ObjectProperty ;
        rdfs:domain :Pessoa ;
        rdfs:range :Pessoa .


#################################################################
#    Data properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/familia#conjuge
:conjuge rdf:type owl:DatatypeProperty ;
         rdfs:domain :Pessoa ;
         rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#crianca
:crianca rdf:type owl:DatatypeProperty ;
         rdfs:domain :Familia ;
         rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#dataBatismo
:dataBatismo rdf:type owl:DatatypeProperty ;
             rdfs:domain :Pessoa ;
             rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#dataCasamento
:dataCasamento rdf:type owl:DatatypeProperty ;
               rdfs:domain :Familia ;
               rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#dataFalecimento
:dataFalecimento rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Pessoa ;
                 rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#dataNascimento
:dataNascimento rdf:type owl:DatatypeProperty ;
                rdfs:domain :Pessoa ;
                rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#dataSepultura
:dataSepultura rdf:type owl:DatatypeProperty ;
               rdfs:domain :Pessoa ;
               rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#divorcio
:divorcio rdf:type owl:DatatypeProperty ;
          rdfs:domain :Familia ;
          rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#esposa
:esposa rdf:type owl:DatatypeProperty ;
        rdfs:domain :Familia ;
        rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#esposo
:esposo rdf:type owl:DatatypeProperty ;
        rdfs:domain :Familia ;
        rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#familiaComoConjuge
:familiaComoConjuge rdf:type owl:DatatypeProperty ;
                    rdfs:domain :Pessoa ;
                    rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#familiaComoFilho
:familiaComoFilho rdf:type owl:DatatypeProperty ;
                  rdfs:domain :Pessoa ;
                  rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#filho
:filho rdf:type owl:DatatypeProperty ;
       rdfs:domain :Pessoa ;
       rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#idFamilia
:idFamilia rdf:type owl:DatatypeProperty ;
           rdfs:domain :Familia ;
           rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#idPessoa
:idPessoa rdf:type owl:DatatypeProperty ;
          rdfs:domain :Pessoa ;
          rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#localBatismo
:localBatismo rdf:type owl:DatatypeProperty ;
              rdfs:domain :Pessoa ;
              rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#localCasamento
:localCasamento rdf:type owl:DatatypeProperty ;
                rdfs:domain :Familia ;
                rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#localFalecimento
:localFalecimento rdf:type owl:DatatypeProperty ;
                  rdfs:domain :Pessoa ;
                  rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#localNascimento
:localNascimento rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Pessoa ;
                 rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#localSepultura
:localSepultura rdf:type owl:DatatypeProperty ;
                rdfs:domain :Pessoa ;
                rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#refn
:refn rdf:type owl:DatatypeProperty ;
      rdfs:domain :Pessoa ;
      rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/familia#sexo
:sexo rdf:type owl:DatatypeProperty ;
      rdfs:domain :Pessoa ;
      rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia#titulo
:titulo rdf:type owl:DatatypeProperty ;
        rdfs:domain :Pessoa ;
        rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/familia/nome
:nome rdf:type owl:DatatypeProperty ;
      rdfs:domain :Pessoa ;
      rdfs:range xsd:string .


#################################################################
#    Classes
#################################################################

###  http://rpcw.di.uminho.pt/2024/familia#Familia
:Familia rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/familia/Pessoa
:Pessoa rdf:type owl:Class .


#################################################################
#    Individuals
#################################################################
'''

for person in root.findall("person"):

    person_id = person.find('id').text

    ttl += f'''\n###  http://rpcw.di.uminho.pt/2024/familia#{person_id}
:{person_id} rdf:type owl:NamedIndividual ,
    :Pessoa ;'''
    
    ttl += f'\n    :idPessoa "{person_id}" ;'
    
    if person.find('name') != None:
        name = person.find('name').text.replace('"',"'")
        ttl += f'\n    :nome "{name}" ;'

    for parent in person.findall('parent'):
        ref = parent.get('ref')
        ttl += f'\n    :{sexProp[sex[ref]]} :{ref} ;'

    if person.find('titl') != None:
        ttl += f'\n    :titulo "{person.find("titl").text}" ;'

    if person.find('sex') != None:
        ttl += f'\n    :sexo "{person.find("sex").text}" ;'

    if person.find('birthdate') != None:
        ttl += f'\n    :dataNascimento "{person.find("birthdate").text}" ;'

    if person.find('birthplace') != None:
        ttl += f'\n    :localNascimento "{person.find("birthplace").text}" ;'
    
    if person.find('deathdate') != None:
        ttl += f'\n    :dataFalecimento "{person.find("deathdate").text}" ;'

    if person.find('deathplace') != None:
        ttl += f'\n    :localFalecimento "{person.find("deathplace").text}" ;'
    
    if person.find('burialplace') != None:
        ttl += f'\n    :localSepultura "{person.find("burialplace").text}" ;'

    if person.find('refn') != None:
        ttl += f'\n    :refn "{person.find("refn").text}"^^xsd:int ;'

    if person.find('familyasspouse') != None:
        ttl += '\n    :familiaComoConjuge '
        asspouses = person.findall('familyasspouse')
        for i in range(0,len(asspouses)):
            ttl += f'"{asspouses[i].text}" ,\n                        '
        ttl = ttl[:-26] + ";"

    if person.find('familyaschild') != None:
        ttl += f'\n    :familiaComoFilho "{person.find("familyaschild").text}" ;'

    if person.find('spouse') != None:
        ttl += '\n    :conjuge '
        spouses = person.findall('spouse')
        for i in range(0,len(spouses)):
            name = spouses[i].text.replace('"',"'")
            ttl += f'"{name}" ,\n             '
        ttl = ttl[:-15] + ";"

    if person.find('child') != None:
        ttl += '\n    :filho '
        children = person.findall('child')
        for i in range(0,len(children)):
            name = children[i].text.replace('"',"'")
            ttl += f'"{name}" ,\n           '
        ttl = ttl[:-13] + ";"

    if person.find('christeningdate') != None:
        ttl += f'\n    :dataBatismo "{person.find("christeningdate").text}" ;'
    
    if person.find('christeningplace') != None:
        ttl += f'\n    :localBatismo "{person.find("christeningplace").text}" ;'

    if person.find('burialdate') != None:
        ttl += f'\n    :dataSepultura "{person.find("burialdate").text}" ;'

    ttl = ttl[:-1] + ".\n"


for family in root.findall('family'):

    ttl += f'''\n###  http://rpcw.di.uminho.pt/2024/familia#{family.find("id").text}
:{family.find("id").text} rdf:type owl:NamedIndividual ,
    :Familia ;'''

    ttl += f'\n    :idFamilia "{family.find("id").text}" ;'

    if family.find('husb') != None:
        name = family.find('husb').text.replace('"',"'")
        ttl += f'\n    :esposo "{name}" ;'

    if family.find('wife') != None:
        name = family.find('wife').text.replace('"',"'")
        ttl += f'\n    :esposa "{name}" ;'

    if family.find('chil') != None:
        ttl += '\n    :crianca '
        children = family.findall('chil')
        for i in range(0,len(children)):
            name = children[i].text.replace('"',"'")
            ttl += f'"{name}" ,\n             '
        ttl = ttl[:-15] + ";"

    if family.find('div') != None:
        ttl += f'\n    :divorcio "{family.find("div").text}" ;'

    if family.find('marr') != None:
        if family.find('marr').find('date') != None:
            ttl += f'\n    :dataCasamento "{family.find("marr").find("date").text}" ;'
        if family.find('marr').find('place') != None:
            ttl += f'\n    :localCasamento "{family.find("marr").find("place").text}" ;'

    ttl = ttl[:-1] + ".\n"

print(ttl)