from rdflib import Graph
from rdflib.plugins import sparql
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class OpenWordnetpt:
	
	def synsets(self, word):
		synsets = []
		#word = 'cachorro'
		stringSparqlQuery = """
			select distinct ?word ?sspt ?lexico where {
				?word
				<https://w3id.org/own-pt/wn30/schema/lexicalForm>
				\""""+word+"""\"@pt .
				?sspt
				<https://w3id.org/own-pt/wn30/schema/containsWordSense>/<https://w3id.org/own-pt/wn30/schema/word>
				?word .
				?ssen
				<http://www.w3.org/2002/07/owl#sameAs>
				?sspt .
				?ssen
				<https://w3id.org/own-pt/wn30/schema/lexicographerFile>
				?lexico .
			}
		"""
		queryString = sparql.prepareQuery(stringSparqlQuery)
		syns = graph.query(queryString)
		for s in syns:
			synsets.append(str(s[0]))
			synsets.append(str(s[1]))
			synsets.append(str(s[2]))
		return synsets #return array of synsets

wordnetpt   = OpenWordnetpt()
graph 		= Graph()
graph.parse("own-pt.nt", format="nt")

sentence = "O homem cachorro que mudou o mundo"

words = set(word_tokenize(sentence.lower()))

lexicos = []

for word in words:
	lexicos.append(wordnetpt.synsets(word))

for lexico in lexicos:
	print(lexico)