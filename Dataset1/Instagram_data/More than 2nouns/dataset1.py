import pickle
import re
from konlpy.tag import Okt
from collections import Counter

okt = Okt()

with open('test.txt') as f:
    line_num=1
    line = f.readline()
    totalPostList = []

    while line:
        #을 기준으로 나눔
        head, sep, tail = line.partition('#')
        resultList =  okt.nouns(head)
        #게시글 저장
        with open('stopwords.txt','r') as f3:
            b=f3.read().split()
            for i in b:
                if i in resultList:
                    resultList.remove(i)
        

        
                    
        line=f.readline()
        line_num+=1


        if len(resultList)>1:
            totalPostList.append(resultList)


    with open('data_1.bin','wb') as f2:
        pickle.dump(totalPostList, f2)


    
print ('Data_2:')
with open('data_1.bin', 'rb') as f:
    data = pickle.load(f)
print (data[:20])   
print ()

print(len(data))


