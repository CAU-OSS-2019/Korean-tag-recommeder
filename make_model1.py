from gensim.models import Word2Vec
import pickle
import time

def main():
    
    # 데이터셋 불러옴
    with open('./Dataset1/insta_noun.bin', 'rb') as f:
        data1 = pickle.load(f)
    with open('./Dataset1/wiki_tokened.bin', 'rb') as f2:
        data2 = pickle.load(f2)

    print("length1:", len(data1), "\nlength2:", len(data2))
    sentences = data1 + data2
    
    start_time = time.time()
    
    # Word2Vec 모델 제작
    print("Making model...")
    model1 = Word2Vec(sentences, size=300, window=5, min_count=5, workers=4, sg=1)

    # 모델 저장
    save_dir = 'Model1_word2vec.model'
    model1.save(save_dir)

    end_time = time.time()
    print("WorkingTime: {0:0.2f} sec\n".format(end_time-start_time))

    # 테스트
    test_word = '카메라'
    print(test_word, ": ")
    ex = model1.wv.most_similar(test_word)
    print(ex)

	# 저장 확인
    test_model = Word2Vec.load(save_dir)
    ex1 = test_model.wv.most_similar(test_word)
    print(ex1)


if __name__ == '__main__':
    main()
