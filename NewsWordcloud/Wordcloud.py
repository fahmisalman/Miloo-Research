from wordcloud import WordCloud, STOPWORDS
# from scipy.misc import
from NewsWordcloud.Preprocessing import *
import matplotlib.pyplot as plt
import glob
import time


class PyWordCloud(object):

    def __init__(self, mask, text, background='white'):
        self.mask = mask
        self.text = text
        self.wordcloud = None
        self.background = background

    def preprocessing(self, d):
        d = d[2:-1].lower()
        d = remove_escape(d)
        d = remove_url(d)
        d = remove_punctuation(d)
        d = stopword_removal(d)
        return d

    def add_image_mask(self,path):
        # generate image
        """
        image should be png with background white and forground black
        :param path: path of image
        :return: image masking
        """
        image_mask = np.array(
            Image.open(path))

        def transform_format(val):
            if val == 0:
                return 255
            else:
                return val

        # Transform your mask into a new one that will work with the function:
        transformed_image_mask = np.ndarray((image_mask.shape[0], image_mask.shape[1]), np.int32)

        for i in range(len(transformed_image_mask)):
            transformed_image_mask[i] = list(map(transform_format, image_mask[i]))

        return transformed_image_mask

    def fit(self):

        words = self.preprocessing(self.text)
        mask = self.add_image_mask(self.mask)

        self.wordcloud = WordCloud(
            background_color=self.background,
            mask=mask
        ).generate(words)

    def view_wordcloud(self, show=True, save=False):
        plt.imshow(self.wordcloud)
        plt.axis('off')
        if save:
            plt.savefig('Output/.png'.format(self.username), dpi=3000)
        if show:
            plt.show()

