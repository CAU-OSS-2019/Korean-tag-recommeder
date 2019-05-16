    from gensim.models import Word2Vec
    #sklearn things--------------------------------------
    from sklearn import cluster
    from sklearn import metrics
    from nltk.cluster import KMeansClusterer
    import nltk
    #--------------------------------------------------------------------
    NUM_CLUSTERS = 3
    
    model = Word2Vec.load("test_word2vec_1.model")
    model_data = model[model.wv.vocab] #word2vec 모델을 kmeans clustering 하기 위하여 데이터로 변환 
    
    # 클러스터링이 잘 되는지 확인-------------------------------------------------------------------------
    kclusterer = KMeansClusterer(NUM_CLUSTERS, distance=nltk.cluster.util.cosine_distance, repeats=25)
    assigned_clusters = kclusterer.cluster(model_data, assign_clusters=True)
    print(assigned_clusters)
 
    words = list(model.wv.vocab)
    for i, word in enumerate(words):
        print(word + ":" + str(assigned_clusters[i]))
    #-----------------------------------------------------------------------------------------------------
     
    #model_data->get Vector Data
    
    # clusterling -------------------------------------------------------------------------------------------
    kmeans = cluster.KMeans(n_clusters=NUM_CLUSTERS)
    kmeans.fit(model_data) #clusterling
    labels = kmeans.labels_ # 각 데이터의 라벨 값들
    centroids = kmeans.cluster_centers_ #각 cluster의 중심점의 좌표
    
    # 결과 확인 -------------------------------------------------------------------------------------------
    print("Cluster id labels for inputted data")
    print(labels)
    print("Centroids data")
    print(centroids)
    #-------------------------------------------------------------------------------------------
    
    
