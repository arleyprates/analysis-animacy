from rdflib import Graph
from rdflib.plugins import sparql
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import annotated_tokens as toks
import time

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
print("\nCarregando grafo da Wordnet na memoria...")
print("Isso pode levar em torno de 6 minutos ou mais.")
graph.parse("own-pt.nt", format="nt")

H_lexicos = []
A_lexicos = []
I_lexicos = []

print("\n# RETORNO DOS LEXICOS PARA OS TOKENS HUMANOS:\n") 
time.sleep(2)
for tk in toks.H_tokens:
    H_lexicos.append(wordnetpt.synsets(tk))
    print("TOKEN: {}".format(tk))
    print("LEXICO: {}".format(wordnetpt.synsets(tk)))
print("\n# RETORNO DOS LEXICOS PARA OS TOKENS DE OUTROS ANIMADOS:\n") 
time.sleep(2)
for tk in toks.A_tokens:
    A_lexicos.append(wordnetpt.synsets(tk))
    print("TOKEN: {}".format(tk))
    print("LEXICO: {}".format(wordnetpt.synsets(tk)))
print("\n# RETORNO DOS LEXICOS PARA OS TOKENS INANIMADOS:\n")
time.sleep(2)
for tk in toks.I_tokens:
    I_lexicos.append(wordnetpt.synsets(tk))
    print("TOKEN: {}".format(tk))
    print("LEXICO: {}".format(wordnetpt.synsets(tk)))

'''
print(len(H_lexicos))
print(H_lexicos[0][-1])
print(len(A_lexicos))
print(A_lexicos[0])
print(len(I_lexicos))
print(I_lexicos[0])
'''
