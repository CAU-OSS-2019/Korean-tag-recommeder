#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import re
import json 
from konlpy import tag
from konlpy.utils import csvwrite, pprint
from konlpy.tag import Mecab
from konlpy.tag import Hannanum
from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Okt
from collections import Counter

if __name__=='__main__':

    okt = Okt()
    mecab = Mecab()
    hannanum = Hannanum()
    kkma = Kkma()
    #komoran = Komoran(userdic='/tmp/dic.txt')

    with open('필카.json') as data_file: #json 파일명
   
        data = json.load(data_file)

   
    for i in data["posts"]:
       
        taggers = [t for t in dir(tag) if t[0].isupper()]

        post = i["caption"] #값 하나하나 접근하기
        # sample = data["posts"][0]"tags"] 이런식으로 접근함
	#data는 json 전체를 dictionary 형태로 저장하고 있음

        post = re.sub('(?:\s)#[^, ]*', '', post)
        # # 태그 제거


    resultList = okt.nouns(post)
    #사용가능 ex) kkma.nouns(post)
    result = '  '.join(unicode(e) for e in resultList)
	#리스티 형식으로 리턴이 되어 유니코드로 변환 .
	

    resultstr = result.encode("UTF-8")
	#뭐같은 유니코디  - 문자열 변환 과정

	#pprint(result)

	#print(type(result))

    with open('stopwords.txt','r') as f:
        a=resultstr.split();b=f.read().split()
        with open('Data_1_1.txt','a') as f:
           f.write(' '.join(i for i in a if i.lower() not in (x.lower() for x in b))+'\r\n\r\n')    
	    
    
    with open('Data_1_1.txt', 'r') as f:
        words = [w.strip('.,') for w in f.read().split()]

    for w, c in Counter(words).most_common(100):
        # print(w, c)
        with open('Data_1_2.txt', 'a') as f:
            f.write(w +':' + str(c)  + '\r\n\r\n')
        







