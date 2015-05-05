# -*- coding: latin-1 -*-
import sys

arquivo = sys.argv[1]
novoArquivo = open(sys.argv[2], 'a')
s = set()

with open (arquivo) as f:
	for line in f:
		if line not in s:	
			#Informe a categoria especificada
			categoria = "Outros"
			corpo = line.strip().split('\t')[0]
			dataDeCriacao = line.strip().split('\t')[1]								
			novoArquivo.write(line)
			s.add(line)
novoArquivo.close()
