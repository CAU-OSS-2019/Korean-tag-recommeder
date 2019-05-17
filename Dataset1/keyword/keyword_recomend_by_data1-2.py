import pickle

from collections import Counter

keyword_num =2

def search_key(count_list, freq_data, loop):
    keep = []
    freq  = []
    key = []
    keyword = []
    count = 0
    i = 0
    
    if (loop >= keyword_num) | (len(count_list) == 0) :
        return 0
    word = list(count_list)
    max_freq = count_list.most_common(1)[0][1]
    while i < len(word) :
        if  max_freq == count_list[word[i]] :
            keep.append(word[i])
            del count_list[word[i]] 
            count = count + 1
        i= i+1
    if count > keyword_num - loop :
        for m in keep :
            freq.append(freq_data[m])
        for v in range(0, keyword_num - loop) :
            index = freq.index(max(freq))
            del freq[index]
            key.append(keep.pop(index))
        keyword.append(key)
    elif count == keyword_num - loop :
        keyword.append(keep)
    elif count < keyword_num - loop :
        keyword.append(keep)
        search_error = search_key(count_list, freq_data, loop + count)
        if(type(search_error) == type(keyword)) :
            keyword.extend(search_error)
    
    return keyword
        

def main():
    
    with open('./opensource/Data_1-1.bin', 'rb') as f:
        letter_data = pickle.load(f)
        
    with open('./opensource/Data_1-2.bin', 'rb') as f2:
        freq_data = pickle.load(f2)

    keyword = []
    loop = 0
    
    for i in range(0, len(letter_data)) :
        count_list = Counter(letter_data[i])
        keyword.append(search_key(count_list, freq_data, loop))
    print(keyword)
    
main()
