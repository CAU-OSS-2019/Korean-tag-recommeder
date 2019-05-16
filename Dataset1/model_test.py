# 모델 학습결과 확인용

from gensim.models import Word2Vec

model_name = 'test_word2vec_1_3k.model'
test_model = Word2Vec.load(model_name)
print("\n***If you want stop, input \'q\'***")
#word = input('words: ')
word = ''

while(True):
	try:
		word = input('\nwords: ')
		if word == 'q':
			break
		result = test_model.wv.most_similar(word)		
	except KeyError as e:
		print(e)
		continue
	
	print(result)
