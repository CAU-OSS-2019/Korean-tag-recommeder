#! /usr/bin/python3.6
# -*- coding: utf-8 -*-

'''
게시글만 가져온 json 파일 전처리용
'''

import re
import json 
import pickle
from konlpy import tag
from konlpy.tag import Okt
from collections import Counter

# 이모지 처리
def strip_e(st):
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    return RE_EMOJI.sub(r'', st)

def main():

    okt = Okt()

    with open('필카.json','rt', encoding='UTF8') as data_file: 
   
        data = json.load(data_file)

    totalPostList = [] 
    totalTagList = []
    totalCountList = []

    for i in data["posts"]:   
        
        post = i["caption"] 
        tags = i["tags"]
       
        if len(tags) < 15:
            
            post = strip_e(post)
            post = re.sub('(?:\s)#[^, ]*', '', post)
             
            resultList =  okt.nouns(post)
            
            with open('stopwords.txt','rt', encoding='UTF8') as f:
                b=f.read().split()
                for i in b:
                    if i in resultList:
                        resultList.remove(i)

            if resultList:
                totalPostList.append(resultList)
                totalTagList.append(resultList+tags)
                totalCountList += (list(set(resultList)))

    #nouns of post only
    with open('Data_1-1.bin', 'wb') as f:
        pickle.dump(totalPostList, f)

    #frequency count 
    countList  = (Counter(totalCountList))

    delete = [] 
    for key, val in countList.items(): 
        if val < 5: 
            delete.append(key) 
          
    for i in delete: 
        del countList[i] 

    
    with open('Data_1-2.bin', 'wb') as f:
        pickle.dump(countList, f)

    # nouns + tags 
    with open('Data_1-3.bin', 'wb') as f:
        pickle.dump(totalTagList, f)

## TEST###################################LINE

    print ('Data_1-1:')
    with open('Data_1-1.bin', 'rb') as f:
        data = pickle.load(f)
    print (data[:5])   
    print ()

    print ('Data_1-2:')
    with open('Data_1-2.bin', 'rb') as f:
        data = pickle.load(f)  
    for i in data.most_common(5):
        print(i)
    print () 

    print ('Data_1-3:')
    with open('Data_1-3.bin', 'rb') as f:
        data = pickle.load(f)
    print (data[:5])   
    print ()


if __name__ == '__main__':
    main()