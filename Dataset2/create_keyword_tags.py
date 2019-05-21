import pickle

from collections import Counter

def main():
    
    with open('keyword.bin', 'rb') as f:
        data = pickle.load(f)
        
    with open('./data1&2/data_2.bin', 'rb') as f2:
        tag = pickle.load(f2)
    
    data2 = [];
    
    for i in range(0, len(tag)) :
        data2.append(data[i] + tag[i])
    
    # 결과 리스트 저장
    save_dir = 'new_data2.bin'  # 저장 경로
    with open(save_dir, 'wb') as fwrite:
        pickle.dump(data2, fwrite)

    fwrite.close()


    # 전처리한 데이터 불러와서 잘 저장되었는지 확인
    with open(save_dir, 'rb') as f:
        pout = pickle.load(f)  # 한 줄씩 읽어옴

    for i in range(5):  # 5줄만 테스트로 읽어옴
        print(pout[i])

    f.close()
    
    
    
main()
