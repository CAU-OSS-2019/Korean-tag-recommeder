# Korean-tag-recommeder  

A prototype of the program recommend the appropriate KOREAN HASHTAGS depending on Instagram body  
Recommend word hashtags that are popular  
but not appearing in the text for the text related to '필카', using Word2Vec model.  
<br>
인스타그램에 업로드할 본문을 입력하면, 해당 본문에 적절한 한글 해쉬태그를 추천하는 프로그램입니다.  
이 프로그램은 prototype으로, '필카'에 관련된 본문에 대한 태그만을 추천합니다.  
인기가 많으면서도 본문에 등장하지 않는 단어를 태그로 추천합니다.  

\* '필카' means short for film camera.  
\* 'Instagram body' means Instagram post without hashtags.  

### example:  

input:  

    오늘 한강. 너무 예쁘다. 역시 필름카메라 감성 최고

output:  

    #한강 #한강공원 #필카 #필름카메라 #film  

<br>

## What Does This Repository Contain  

![Workflow](https://github.com/CAU-OSS-2019/team-project-team18/blob/master/Modeling%20Workflow.jpg)

* `Dataset1/` data for Model 1  
  * `kowiki_data_tokenizing.py' Tokenize Korean Wiki text file  
* `Dataset2/` data for Model 2  
  * `keyword_recomend_by_counted.py` Choose keyword from `insta_noun.bin` by `insta_counted.bin'
  * `create_keyword_tags.py` create `keyword_tags.bin` for Model 2  

* `Model1_word2vec.model` Model 1 for recommending WORDS similar to the keywords  
* `Model2_word2vec.model` Model 2 for recommending TAGS related to keywords  
* `make_model1.py` Make Model 1  
* `make_model2.py` Make Model 2  
* `model_test.py` Check the results of the model created  



<br>  

## Manual  

### Environment configuration  
Run in your terminal (recommended):  

    pip install --upgrade gensim

or, alternatively for conda environments:  

    conda install -c conda-forge gensim

<br>

For preprocessing of data, you need to install KoNLPy:

    pip install --upgrade pip
    conda -c conda-forge install jpype1

    pip install konlpy

### Testing

    Testmodel.py #교체예정!!

<br>

For more instructions of PREPROCESSING/MODELING, please see [WIKI](https://github.com/CAU-OSS-2019/team-project-team18/wiki)

<br>
