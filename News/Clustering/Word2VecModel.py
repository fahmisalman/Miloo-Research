from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
import numpy as np
import os


class Word2VecModel(object):

    def __init__(self):
        self.x = []
        self.x_prep = []
        self.model = None

    def fit(self, x, sizes=300, windows=5, epoch=10, save=False, filename='', sg=True):
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

        self.x = x
        self.x_prep = []

        for i, row in enumerate(self.x):
            self.x_prep.append(simple_preprocess(row))

        type = 0

        if sg:
            type = 1

        self.model = Word2Vec(
            self.x_prep,
            size=sizes,
            window=windows,
            min_count=2,
            workers=10,
            sg=type
        )

        self.model.train(self.x_prep, total_examples=len(self.x_prep), epochs=epoch)

        if save:
            if filename == '':
                type_list = ['CBoW', 'Skip-gram']
                self.model.save(os.path.join(os.getcwd(),
                                             'Model/Word2Vec_model={}_sizes={}_windows{}.model'.format(type_list[type],
                                                                                                       sizes,
                                                                                                       windows)))
            else:
                self.model.save(os.path.join(os.getcwd(), 'Model/' + filename))

    def load_w2v_model(self, filename):
        self.model = Word2Vec.load(os.path.join(os.getcwd(), 'Model/' + filename))
        return self.model

    def preprocessing(self, doc):
        return simple_preprocess(doc)

    def document_to_vector(self, doc):
        data = simple_preprocess(doc)
        vector = np.zeros(self.model.vector_size)
        for word in data:
            if word in self.model.wv.vocab:
                vector += self.model[word]
        return vector
