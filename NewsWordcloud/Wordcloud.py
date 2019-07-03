from wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread
from NewsWordcloud.Preprocessing import *
import matplotlib.pyplot as plt
import glob


class PyWordCloud(object):

    def __init__(self, text, background='white'):
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

    def fit(self):

        words = self.preprocessing(self.text)

        self.wordcloud = WordCloud(
            background_color=self.background
        ).generate(words)

    def view_wordcloud(self, show=True, save=False):
        plt.imshow(self.wordcloud)
        plt.axis('off')
        if save:
            plt.savefig('Output/.png'.format(self.username), dpi=300)
        if show:
            plt.show()


if __name__ == '__main__':

    text = """Kebakaran rumah terjadi permukiman padat penduduk di Kebayoran Baru, Jakarta Selatan. Sebanyak 14 unit mobil pemadam kebakaran dikerahkan ke lokasi.

"Benar ada kebakaran, sudah ada 14 unit ke lokasi termasuk pendukung," kata Petugas Sudin Penanggulangan Kebakaran dan Penyelamatan (PKP) Jakarta Selatan, Sukarno, saat dikonfirmasi, Selasa (2/7/2019).

Lokasi kebakaran terjadi Jl Kebalen VII RT 02/RW 04, Kebayoran Baru, Jakarta Selatan. Kebakaran terjadi sekitar pukul 18.22 WIB.

"Kebakaran di Jalan Kebalen VII. Objek rumah tinggal padat penduduk," ujarnya.

Belum diketahui penyebab pasti kebakaran serta dampak kebakaran itu. Sukarno menyebut petugas sedang melakukan pemadaman api.

"Petugas masih bekerja, situasi masih merah (api menyala, red)," sebutnya."""

    wc = PyWordCloud(text)
    wc.fit()
    wc.view_wordcloud()
