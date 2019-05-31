from NewsClustering import Data_processing, Word2VecModel, MultidocSummary
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

    x_words = []
    for row in x:
        x_words.append(w2v.preprocessing(row))

    list_label = list(set(clf.labels_))

    for i in range(len(list_label)):

        docs = []

        for j in range(len(clf.labels_)):

            if clf.labels_[j] == list_label[i]:
                docs.append(x[j])

        print(MultidocSummary.fit(docs))

