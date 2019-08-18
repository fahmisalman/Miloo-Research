from Preprocessing import Preprocessing
from wordcloud import WordCloud
from scipy.misc import imread
import matplotlib.pyplot as plt
import os


class PyWordCloud(object):

    def __init__(self, background='white', mask=None, font=None, max_word=200):
        self.mask = mask
        self.font = font
        self.max_word = max_word
        self.text = ''
        self.wordcloud = None
        self.background = background

    def preprocessing(self, d):
        """
        Remove unnecessary characters and words in the dataset

        :param d: text (sentence, documents, news text, etc)
        :return: text that has been cleaning from unnecessary characters and words
        """
        pre = Preprocessing.Preprocessing()
        d = d[2:-1].lower()
        d = pre.remove_escape(d)
        d = pre.remove_url(d)
        d = pre.remove_punctuation(d)
        d = pre.stopword_removal(d)
        d = pre.join_input(d)
        return d

    def fit(self, text):
        """
        Generate the wordclouds

        :param text: text that will be generated
        """

        self.text = text
        mask_img = None

        if self.font is None:
            self.font = os.path.join(os.getcwd(), 'News/Wordcloud/Assets/Font/CabinSketch-Bold.ttf')

        if self.mask is None:
            width = 400
            height = 200
            mask_img = imread(os.path.join(os.getcwd(), 'News/Wordcloud/Assets/Mask/jap.jpg'), flatten=True)
        else:
            mask_img = imread(self.mask, flatten=True)
            height = mask_img.shape[0]
            width = mask_img.shape[1]

        words = self.preprocessing(self.text)

        self.wordcloud = WordCloud(
            background_color=self.background,
            width=width,
            height=height,
            mask=mask_img,
            font_path=self.font,
            max_words=self.max_word
        ).generate(words)

    def view_wordcloud(self, show=True, save=False, filename=''):
        """
        Show or/and save the Wordcloud

        :param show: show the wordclouds if conditions is True
        :param save: save the wordclouds if conditions is True
        :param filename: filename of the wordclouds that will be saved
        """
        plt.imshow(self.wordcloud)
        plt.axis('off')
        if filename == '':
            filename = 'Out_image'
        if save:
            plt.savefig('Output/{}.png'.format(filename), dpi=3000)
        if show:
            plt.show()

