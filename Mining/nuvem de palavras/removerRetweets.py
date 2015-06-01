# -*- coding: latin-1 -*-
import sys

replace = [('RT', '')]

#Remover retweets
def removeRetweets(text):
	para = text
	for (lat, asc) in replace:
		para = para.replace(lat, asc)
	return para

arquivo = sys.argv[1]
novoArquivo = open(sys.argv[2], 'a')
s = set()

with open (arquivo) as f:
	for line in f:
		if line not in s:
			categoria = line.strip().split('\t')[0]
			texto = line.strip().split('\t')[1]
			corpo = removeRetweets(texto)
			novoArquivo.write('%s\t%s\n' %(categoria,corpo))
			s.add(line)
novoArquivo.close()
