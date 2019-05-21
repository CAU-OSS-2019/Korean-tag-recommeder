import pickle
from collections import Counter

#------------------------------------------------

# 한 게시글 당 뽑을 키워드의 갯수
keyword_num =2 

# keyword 찾는 함수

# count_list = data1-1의 게시글 하나를 저장한 counter
# freq_data = data1-2
# loop = search_key 반복 제어 변수
def search_key(count_list, freq_data, loop): 
    
    keep = [] # 게시글 내에서 가장 높은 빈도로 등장하는 명사를 저장하는 list
    freq  = [] # data1-2를 통해 keep에 있는 명사들이 전체 게시글에서 등장하는 빈도를 저장하는 list
    key = [] # 게시글 하나의 keyword 리스트
    keyword = [] # keyword 리스트
    count = 0 # 게시글 내에 가장 높은 빈도를 가진 명사의 수
    i = 0 # 반복문 제어 변수
    
    # 키워드를 다 뽑았거나 게시글의 단어가 더 없다면 종료
    if (loop >= keyword_num) | (len(count_list) == 0) :
        return 0
    
    word = list(count_list) #count_list에서 명사들을 list로 만듦
    max_freq = count_list.most_common(1)[0][1] # 한 게시글 내에서 가장 많이 등장한 단어의 빈도
    while i < len(word) :
        if  max_freq == count_list[word[i]] : # word[i]가 가장 많이 등장했다면
            keep.append(word[i])
            del count_list[word[i]] # count_list에서 word[i] 삭제 
            count = count + 1
        i= i+1
    if count > keyword_num - loop : # 게시글 내에서 가장 많이 등장한 단어가 뽑아야할 키워드의 수보다 많을 경우
        for m in keep :
            freq.append(freq_data[m]) 
        for v in range(0, keyword_num - loop) :
            index = freq.index(max(freq)) # 전체 게시글에서 가장 많이 등장한 단어의 index를 뽑는다
            del freq[index]
            key.append(keep.pop(index)) # 전체 게시글에서 가장 많이 등장한 단어를 keyword로 선정한다
        keyword.extend(key) #append => extend로(변경)
    elif count == keyword_num - loop : # 게시글 내에서 가장 많이 등장한 단어가 뽑아야할 키워드의 수와 같을 경우
        keyword.extend(keep) #append => extend로(변경)
    elif count < keyword_num - loop : # 게시글 내에서 가장 많이 등장한 단어가 뽑아야할 키워드의 수보다 적을 경우
        search_error = search_key(count_list, freq_data, loop + count) # 더 키워드를 뽑는다.
        if(type(search_error) == type(keyword)) : # return값이 list가 아니면
            keep.extend(search_error) # keep에 추가하지 않는다. #keyword => keep으로 (변경)
        keyword.extend(keep) #append => extend로 & 위치 바꿈 (변경)           
    
    return keyword
        

def main():
    
    with open('../Dataset1/insta_noun.bin', 'rb') as f:
        letter_data = pickle.load(f)
        
    with open('../Dataset1/insta_counted.bin', 'rb') as f2:
        freq_data = pickle.load(f2)

    keyword = []
    loop = 0
    
    for i in range(0, len(letter_data)) :
        count_list = Counter(letter_data[i])
        keyword.append(search_key(count_list, freq_data, loop))

    # 결과 리스트 저장
    save_dir = 'keyword.bin'  # 저장 경로
    with open(save_dir, 'wb') as fwrite:
        pickle.dump(keyword, fwrite)

    fwrite.close()


    # 전처리한 데이터 불러와서 잘 저장되었는지 확인
    with open(save_dir, 'rb') as f:
        data = pickle.load(f)  # 한 줄씩 읽어옴

    for i in range(5):  # 5줄만 테스트로 읽어옴
        print(data[i])

    f.close()
    
    
main()
