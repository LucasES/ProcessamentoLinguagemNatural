# -*- coding: latin-1 -*-
import sys

arquivo = sys.argv[1]
novoArquivo = open(sys.argv[2], 'a')
s = set()

with open (arquivo) as f:
	for line in f:
		if line not in s:
			corpo = line.strip().split('\t')[0]
			dataDeCriacao = line.strip().split('\t')[1]								
			novoArquivo.write('%s\t%s\n' %(corpo, dataDeCriacao))
			s.add(line)
novoArquivo.close()
