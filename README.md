# Korean-tag-recommeder  

A prototype of the program recommend the appropriate KOREAN TAGS depending on Instagram body  
Recommend word tags that are popular but not appearing in the text for the text related to '필카', using Word2Vec model  
<br>
인스타그램 본문을 입력하면, 본문에 적절한 한글 태그를 추천하는 프로그램의 prototype입니다.  
'필카'에 관련된 본문에 대해, 인기가 많으면서도 본문에 등장하지 않는 단어를 태그로 추천합니다.

*'필카' means short for film camera

### example:  

input:  

    오늘 한강. 너무 예쁘다. 역시 필름카메라 감성 최고

output:  

    #한강 #한강공원 #필카 #필름카메라 #film  

<br>

## What Does This Repo Contain  
* `Dataset/` Training data
  * `Dataset1/` data for Model 1
  * `Dataset2/` data for Model 2
* `Model/`  

<br>  

## Manual  

### Environment configuration  
Run in your terminal (recommended):  

    pip install --upgrade gensim

or, alternatively for conda environments:  

    conda install -c conda-forge gensim

<br>

For preprocessing of data:

    pip install --upgrade pip
    conda -c conda-forge install jpype1

    pip install konlpy

### Testing

    Testmodel.py

<br>

For more instructions of preprocess/making model please see WIKI(링크)  
<br>


## Contribute  
Before Contribution, please read HERE 



