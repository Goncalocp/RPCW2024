# RPCW2024

* Tema: Cinema

**TPC6**

* Obter informação necessária da DBpedia através de queries sparql 
* Criação de ficheiro JSON com essa informção

* Carregar o dataset no endpoint: "http://epl.di.uminho.pt:7200", no repositório "http://epl.di.uminho.pt:7200/repositories/cinema2024"

* Construir queries SPARQL para responder às perguntas:
   - Quantos filmes existem no repositório?
   - Qual a distribuição de filmes por ano de lançamento?
   - Qual a distribuição de filmes por género?
   - Em que filmes participou o ator "Burt Reynolds"?
   - Produz uma lista de realizadores com o seu nome e o número de filmes que realizou
   - Qual o título dos livros que aparecem associados aos filmes?

* Usar o flask para gerar uma interface web no repositório de filmes (obrigatório usar o endpoint definido no ínicio)