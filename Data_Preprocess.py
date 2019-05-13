#! /usr/bin/python3.6
# -*- coding: utf-8 -*-

import re
import json 
import pickle
from konlpy import tag
from konlpy.tag import Okt
from collections import Counter

if __name__=='__main__':

    okt = Okt()

    with open('필카.json') as data_file: 
   
        data = json.load(data_file)

    totalPostList = [] 
    totalTagList = []
    totalCountList = []

    for i in data["posts"]:
       
        
        post = i["caption"] 
        tags = i["tags"]
       

        if len(tags) < 15:
            
            post = re.sub('(?:\s)#[^, ]*', '', post)
             
            resultList =  okt.nouns(post)
            
            with open('stopwords.txt','r') as f:
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


    with open('Data_1-1.bin', 'rb') as f:
        data = pickle.load(f)
        print (data) 
    print ('######################')

    with open('Data_1-2.bin', 'rb') as f:
        data = pickle.load(f)
        for i,j in data.items():
            print (Counter(countList)) # sorted print 

    print ('######################') 
    with open('Data_1-3.bin', 'rb') as f:
        data = pickle.load(f)
        print (data) 



    


      
	    
    
   






                  
