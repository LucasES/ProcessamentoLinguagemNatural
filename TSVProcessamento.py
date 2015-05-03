# -*- coding: latin-1 -*-
import re
import codecs
import unidecode
import string
import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize.regexp import WhitespaceTokenizer
from nltk.stem import RSLPStemmer

class LimparTexto(object):
	def __init__(self):
		self.portugues_stemmer = RSLPStemmer()
		self.tokenizar = WhitespaceTokenizer()
		self.stopwords = stopwords.words('portuguese')

	#Realiza a remoção das stop words que são palavras que não representam significado para o nosso modelo.
	def removerStopWords(self, texto):		
		texto = ' '.join([word for word in texto.split() if word.decode('latin-1') not in self.stopwords])
		texto = ' '.join([word for word in texto.split() if word.decode('latin-1') not in self.mais_utilizadas])
		return texto

	#Tokenização das palavras por espaços
	def tokenizarPalavras(self, texto):
		texto = self.tokenizar.tokenize(texto)
		return texto

	#A remoção da pontuação é necessário pois palavras seguidas de pontos difere de palavra iguais sem a pontuação.
	def removerPontuacao(self, texto):
		regex = re.compile('[%s]' % re.escape(string.punctuation))
		texto = regex.sub('',texto)
		return texto
		
		
	#Remoção dos sufixos das palavras
	def removerSufixo(self, para):
		#Essa linha só é necessário se não for chamado o método de tokenizarPalavras antes de chamar este método.
		para = self.tokenizar.tokenize(para)
		text = ''
		for w in para:
			text = text + self.portugues_stemmer.stem(w.decode('latin-1')) + ' '
		return text
	
	def removerAcentos(self, texto):
		texto = unicode(texto, 'latin-1')
		para = unidecode.unidecode(texto)
		return para

arquivo = sys.argv[1]
novoArquivo = open(sys.argv[2], 'a')
t = LimparTexto()
s = set()

with open (arquivo) as f:
	for line in f:
		if line not in s:
			idTweet = line.strip().split('\t')[0]
			texto = line.strip().split('\t')[1]
			corpo = t.removerAcentos(texto)
			corpo = t.removerPontuacao(corpo)
			corpo = corpo.lower()
			corpo = t.removerStopWords(corpo)
			corpo = t.removerSufixo(corpo)
			dataDeCriacao = line.strip().split('\t')[2]								
			novoArquivo.write('%s\t%s\t%s\n' %(idTweet, corpo, dataDeCriacao))
			s.add(line)
novoArquivo.close()
	
