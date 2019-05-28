from NewsClustering import Data_processing, Word2VecModel
from sklearn.cluster import KMeans
from collections import Counter
import os


if __name__ == '__main__':

    # Load data pickle and save to csv
    data = Data_processing.load_data('news_dataset_5000.pkl')
    x = []
    for row in data:
        x.append(row['news_body'])
    Data_processing.save2csv('News_dataset.csv', [x])

    # Creating Word2Vec model
    # model = w2v_model(x, save=True)
    # model = get_w2v_model('Word2Vec_model=Skip-gram_sizes=300_windows5')
    w2v = Word2VecModel.Word2VecModel()
    model = w2v.load_w2v_model('Word2Vec_model=Skip-gram_sizes=300_windows5')
    x_train = []
    for row in x:
        x_train.append(w2v.document_to_vector(row))
    Data_processing.save2csv('Vector_data.csv', x_train)

    # Cluster the data
    clf = KMeans(n_clusters=5, random_state=1)
    clf.fit(x_train)
    for i in clf.labels_:
        print(i)

    print(Counter(clf.labels_))
