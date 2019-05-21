'''
위키피디아 한국어 파일을 tokenizing하여 저장.
40분 정도 소요됨.

* 코드 실험을 위해서는 test_kowiki_data_tokenizing.py 구동

'''

from konlpy.tag import Okt
import pickle
import time


def main():
    
    # 데이터파일 잘 읽어와지는지 확인
    data_dir = 'wikiAA.txt'  # 파일 경로
    ftest = open(data_dir, 'r', encoding="utf-8")

    i = 0
    while True:
        line = ftest.readline()
        if line != '\n':
            i = i+1
            print("%d번째 줄 :"%i + line)
        if i == 5:
            break 
    ftest.close()

    # Tokenizing
    okt = Okt()

    # 데이터 파일 읽기
    fread = open(data_dir, 'r', encoding="utf-8")

    n = 0
    result = []
    start_time = time.time()

    while True:
        line = fread.readline()  # 한 줄씩 읽음
        if not line: break # 모두 읽으면 while문 종료
        
        n = n + 1
        if n % 5000 == 0:  # 5,000의 배수로 While문이 실행될 때마다 몇 번째 실행인지 출력
            print("%d번째 While문."%n)

        tokenlist = okt.nouns(line)  # 단어 토큰화, 명사만 리스트에 넣음
        
        with open('stopwords.txt', 'rt', encoding='UTF8') as f:
            b = f.read().split()
            for i in b:
                if i in tokenlist:
                    tokenlist.remove(i)

        if tokenlist:  # 이번에 읽은 데이터에 명사가 존재할 경우에만
            result.append(tokenlist)  # 결과에 저장
    fread.close()

    # 결과 리스트 저장
    save_dir = 'wiki_tokened.bin'  # 저장 경로
    with open(save_dir, 'wb') as fwrite:
        pickle.dump(result, fwrite)
    fwrite.close()

    end_time = time.time()
    print("\n", len(result))
    print("WorkingTime: {0:0.2f} sec\n".format(end_time-start_time))

    # 전처리한 데이터 불러와서 잘 저장되었는지 확인
    with open(save_dir, 'rb') as f:
        data = pickle.load(f)  # 한 줄씩 읽어옴

    for i in range(5):  # 5줄만 테스트로 읽어옴
        print(data[i])

    f.close()


if __name__ == '__main__':
    main()
