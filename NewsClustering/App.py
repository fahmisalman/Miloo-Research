from NewsClustering import LoadData
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
import os


def w2v_model(x, sizes=300, windows=5, epoch=10, save=False, filename='', sg=True):
    """

    :param x:
    :param sizes:
    :param windows:
    :param epoch:
    :param save:
    :param filename:
    :param sg:
    :return:
    """

    type_list = ['CBoW', 'Skip-gram']

    x_prep = []
    for i, row in enumerate(x):
        x_prep.append(simple_preprocess(row))

    type = 0

    if sg:
        type = 1

    model = Word2Vec(
        x_prep,
        size=sizes,
        window=windows,
        min_count=2,
        workers=10,
        sg=type
    )

    model.train(x_prep, total_examples=len(x_prep), epochs=epoch)

    if save:
        if filename == '':
            model.save(os.path.join(os.getcwd(),
                                    'Model/Word2Vec_model={}_sizes={}_windows{}.model'.format(type_list[type],
                                                                                        sizes,
                                                                                        windows)))
        else:
            model.save(os.path.join(os.getcwd(), 'Model/' + filename))

    return model


if __name__ == '__main__':

    # Load data pickle and save to csv
    data = LoadData.load_data('news_dataset_5000.pkl')
    x = []
    for row in data:
        x.append(row['news_body'])
    LoadData.save2csv('News_dataset.csv', [x])

    # Creating Word2Vec model
    model = w2v_model(x, save=True)
