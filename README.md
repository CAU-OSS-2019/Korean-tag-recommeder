# Korean-tag-recommeder

인스타그램 본문을 입력하면, 본문에 적절한 태그를 추천하는 프로그램의 prototype입니다.  
<br>
이 프로그램은 '필카'에 관련된 본문에 대해 인기가 많으면서도 본문에 등장하지 않는 단어의 태그를 추천합니다.


주제어: '필카'  
Dataset: '#필카' 태그를 포함하는 Instagram 게시글  
Model 제작 방법: Word2Vec skip-gram  

input:

    문장
    ex) 오늘 한강. 너무 예쁘다. 역시 필름카메라 감성 최고

output:

    태그
    ex) #한강 #한강공원 #필카 #필름카메라 #film 

