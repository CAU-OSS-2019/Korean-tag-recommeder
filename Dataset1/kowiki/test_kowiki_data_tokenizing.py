# Test용 코드

# 데이터파일 잘 읽어와지는지 확인
import sys

data_dir = 'wiki_data.txt'  # 파일 경로
try:
    ftest = open(data_dir, 'r', encoding="utf-8")
except FileNotFoundError as e:
    print(e)
    print("Run the following command first\n" +
        "    copy .\\wikiA* wiki_data.txt")
    sys.exit()


i = 0
while True:
    line = ftest.readline()
    if line != '\n':
        i = i+1
        print("%d번째 줄 :"%i + line)
    if i == 5:
        break 
ftest.close()


# 전처리 시작

from konlpy.tag import Okt
okt = Okt()

# 데이터 파일 읽기
fread = open(data_dir, 'r', encoding="utf-8")

n = 0
test_num = 10000  # 테스트할 line 수
test_result = []

for i in range(test_num):
    line = fread.readline()  # 한 줄씩 읽음
    if not line: break  # 모두 읽으면 while문 종료
    n = n + 1
    if n % 1000 == 0:  # 1,000의 배수로 While문이 실행될 때마다 몇 번째 실행인지 출력
        print("%d번째 While문."%n)
    tokenlist = okt.pos(line, stem=True, norm=True)  # 단어 토큰화
    temp = []
    for word in tokenlist:
        if word[1] in ["Noun"]:  # 명사일 때만
            temp.append((word[0]))  # 해당 단어 저장

    if temp:  # 이번에 읽은 데이터에 명사가 존재할 경우에만
        test_result.append(temp)  # 결과에 저장
fread.close()

# 결과 리스트 저장
import pickle

save_dir = './'  # 저장 위치.
with open(save_dir + 'test_wiki_tokened.bin', 'wb') as fwrite:
    pickle.dump(test_result, fwrite)

# 전처리한 데이터 불러와서 잘 저장되었는지 확인
tokend_name = 'test_wiki_tokened.bin'
with open(tokend_name, 'rb') as f:
    data = pickle.load(f)  # 단 한줄씩 읽어옴

for i in range(5):  # 10줄만 테스트로 읽어옴
    print(data[i])

f.close()
