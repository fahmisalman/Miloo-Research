from News.Clustering import Data_processing, Word2VecModel, MultidocSummary
from sklearn.cluster import KMeans
import os


def top_n_news(X, y):

    list_label = list(set(y))

    for i in range(len(list_label)):
        docs = []
        for j in range(len(y)):
            if y[j] == list_label[i]:
                docs.append(X[j])

        print("Cluster-{}".format(list_label[i]))
        print(MultidocSummary.fit(docs))


def fit():

    # Load data pickle and save to csv
    data = Data_processing.load_data(os.path.join(os.getcwd(), 'news_dataset_5000.pkl'))
    x = []
    for row in data:
        x.append(row['news_body'])
    Data_processing.save2csv('News_dataset.csv', [x])

    # Creating Word2Vec model
    w2v = Word2VecModel.Word2VecModel()
    w2v.fit(x, save=True)

    # Load Word2Vec model
    w2v = Word2VecModel.Word2VecModel()
    model = w2v.load_w2v_model('Word2Vec_model=Skip-gram_sizes=300_windows5')
    x_train = []
    for row in x:
        x_train.append(w2v.document_to_vector(row))
    Data_processing.save2csv('Vector_data.csv', x_train)

    # Cluster the data
    clf = KMeans(n_clusters=5, random_state=1)
    clf.fit(x_train)

    # Get the characteristic of each cluster
    top_n_news(x, clf.labels_)