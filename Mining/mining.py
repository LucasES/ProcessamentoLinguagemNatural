# -*- coding: latin-1 -*-
import tweepy
import sys
#import threading2
#from timer2 import Timer

def colectTweets():
	CONSUMER_KEY='S12KuMMNZlxDxGAIhgR1LF1l0'
	CONSUMER_SECRET='MBb1xnYITlwdyGvGu6lweaCZGcrUpCaWHzrIgMLLczjEnYgsrm'
	ACCESS_TOKEN_KEY='321078098-8vIQlLJbGldygABIw80AvUAiDI1lTi7ubV3uZLiK'
	ACCESS_TOKEN_SECRET='FaxpT1uPdzkwNmoT7m13Y2W91mLs9mPrP3gYrbRPIrao5'
	auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET)
	api=tweepy.API(auth)

	novoArquivo = open(sys.argv[2], 'a')

	pageCount = 5
	if len(sys.argv) == 3:
		pageCount = int(sys.argv[1])
		dicionario = ['esporte', '#natacao', '#volei', '#basquete', '#brasileirao', '#ufc', '#fight', '#luta', '#mma', '#surf', '#futebol']
		for palavra in dicionario:
			maxId = 999999999999999999999
			for i in range(1, pageCount + 1):
				results = api.search(q='%s' % palavra, max_id=maxId, count=100,result_type='recent', geocode='-28.9216313,-38.3203125,2499.470km')
				for result in results:
					maxId = min(maxId, result.id)
#					print "%s\t%s\t%s" %  (result.id, result.text.encode('latin-1','ignore').replace('\n',' '),result.created_at)
					novoArquivo.write('%s\t%s\n' %  (result.text.encode('latin-1','ignore').replace('\n',' '),result.created_at))

#	t = threading2.Timer(3600,colectTweets)
#	t.start()
	else:
		print "Informe 3 parametros "
	
colectTweets()
