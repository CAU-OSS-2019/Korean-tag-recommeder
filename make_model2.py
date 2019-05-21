from gensim.models import Word2Vec
import pickle


def main():
    # 데이터셋 불러옴
    with open('new_data2.bin', 'rb') as f:
        data = pickle.load(f)

    sentences = data

    # Word2Vec 모델 제작
    model2 = Word2Vec(sentences, size=300, window=1000, min_count=300, workers=4, sg=1)

    # 모델 저장
    save_dir = 'Model2_word2vec.model'
    model2.save(save_dir)

    # 테스트
    test_word = '필카'
    ex = model2.wv.most_similar(test_word,topn= 30)
    print(ex)
    i = 0
    tagList =[]
    while True:
        if i == len(ex): break
        if '#' in ex[i][0]:
            tagList.append(ex[i])
            del ex[i]
        i+=1


    print(tagList)#결과값,추천하는 태그입니다




if __name__ == '__main__':
    main()
