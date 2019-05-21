#DATT.txt ->Data_1-1.bin
#         ->Data_1-2.bin

import pickle
from konlpy.tag import Okt
from collections import Counter

okt = Okt()

with open('DATT.txt') as f:
    line_num=1
    line = f.readline()
    totalPostList = []
    totalCountList = []
    while line:
        resultList =  okt.nouns(line)
        with open('stopwords.txt','r') as f3:
            b=f3.read().split()
            for i in b:
                if i in resultList:
                    resultList.remove(i)
        line=f.readline()
        line_num+=1

        if resultList:
            totalPostList.append(resultList)
            totalCountList += (list(set(resultList)))

    with open('Data_1-1.bin','wb') as f2:
        pickle.dump(totalPostList, f2)

    countList  = (Counter(totalCountList))
    with open('Data_1-2.bin', 'wb') as f4:
        pickle.dump(countList, f4)


    
print ('Data_1-1:')
with open('fin.bin', 'rb') as f:
    data = pickle.load(f)
print (data[:5])   
print ()

print ('Data_1-1:')
with open('Data_1-2.bin', 'rb') as f:
    data = pickle.load(f)
    for i in data.most_common(5):
        print(i)
print ()
