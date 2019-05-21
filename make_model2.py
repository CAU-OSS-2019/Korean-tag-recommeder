from gensim.models import Word2Vec
import pickle
import time


def main():
    # 데이터셋 불러옴
    with open('./Dataset2/keyword_tags.bin', 'rb') as f:
        data = pickle.load(f)
    print("length:", len(data))

    start_time = time.time()

    # Word2Vec 모델 제작
    model2 = Word2Vec(data, size=300, window=1000, min_count=300, workers=4, sg=1)

    # 모델 저장
    save_dir = 'Model2_word2vec.model'
    model2.save(save_dir)

    end_time = time.time()
    print("WorkingTime: {0:0.2f} sec\n".format(end_time-start_time))

    # 테스트
    test_word = '필카'
    print(test_word, ": ")
    ex = model2.wv.most_similar(test_word,topn= 30)
    print(ex)

    # 해쉬태그만 남김
    i = 0
    tagList = []
    while True:
        if i == len(ex): break
        if '#' in ex[i][0]:
            tagList.append(ex[i])
            del ex[i]
        i+=1

    # 결과값, 추천하는 태그 출력
    print(tagList)


if __name__ == '__main__':
    main()
