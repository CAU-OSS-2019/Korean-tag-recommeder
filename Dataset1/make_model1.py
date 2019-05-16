from gensim.models import Word2Vec
import pickle

def main():
    
    with open('./instagram/Data_1-1.bin', 'rb') as f:
        data1 = pickle.load(f)
    with open('./kowiki/test_wiki_tokened.bin', 'rb') as f2:
        data2 = pickle.load(f2)

    sentences = data1 + data2
    model1 = Word2Vec(sentences, size=300, window=5, min_count=5, workers=4, sg=1)

    save_dir = 'test_word2vec_1.model'
    model1.save(save_dir)
    test_word = '카메라'
    ex = model1.wv.most_similar(test_word)
    print(ex)

    # 최종 모델 저장
    
    
	# 저장 확인
    test_model = Word2Vec.load(save_dir)
    ex1 = test_model.wv.most_similar(test_word)
    print(ex1)

if __name__ == '__main__':
    main()
