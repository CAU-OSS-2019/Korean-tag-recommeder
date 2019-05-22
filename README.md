# Korean-tag-recommeder  

A prototype program that recommends appropriate KOREAN HASHTAGS depending on Instagram body  
Recommend word hashtags that are popular but not appearing in the post, using Word2Vec model.  
<br>
인스타그램에 업로드할 본문을 입력하면, 해당 본문에 적절한 한글 해쉬태그를 추천하는 프로그램입니다.  
Word2Vec을 이용한 모델로 많이 사용되면서도 본문에 등장하지 않는 단어를 태그로 추천합니다.  

※ 'Instagram body' means Instagram post without hashtags.  
<br>

## 구현 범위 및 개발 방법  

이 프로그램은 prototype으로, '필카'에 관련된 본문에 대한 태그만을 추천합니다.  
※ '필카': '필름 카메라'의 준말 Short for film camera  

* 개발 언어: Python 3.6  
* 개발 툴: Anaconda, Jupytal Notebook  
* 협업 툴: Github, Slack  
* 사용 라이브러리: KoNLPy, Gensim  

### example:  

input:  

    오늘 한강. 너무 예쁘다. 역시 필름카메라 감성 최고

output:  

    #한강 #한강공원 #필카 #필름카메라 #film  

<br>

# What This Repository Contains  

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

# Manual  

### Environment configuration  
To use Word2Vec, Gensim must be installed.  

  Run in your terminal (recommended):  

    $ pip install --upgrade gensim

  or, alternatively for conda environments:  

    $ conda install -c conda-forge gensim

<br>

For preprocessing of data, you need to install KoNLPy:

    $ pip install --upgrade pip
    $ conda -c conda-forge install jpype1

    $ pip install konlpy

### Testing

    $ Testmodel.py #교체예정!!

<br>

For more instructions of PREPROCESSING/MODELING, please read [WIKI](https://github.com/CAU-OSS-2019/team-project-team18/wiki)  
<br>

# Contribution  
If you want to contribute on our project, please read [Contribution Guide](https://github.com/CAU-OSS-2019/team-project-team18/blob/master/Contribution_Guide.md) before Contributing.  

<br>
