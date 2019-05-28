from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re
import os


class Preprocessing(object):

    def __init__(self):
        self.factory = StemmerFactory()
        self.stemmer = self.factory.create_stemmer()
        self.stopwords = [line.rstrip('\n\r') for line in open(os.path.join(os.getcwd(), 'stopwords.txt'))]

    def casefolding(self, sentence):
        """
        Transform words from uppercase into lowercase and remove characters other than letters.

        :param sentence: sentence that will be transform
        :return: lowercase sentence and only contain letters
        """
        sentence = sentence.lower()
        sentence = re.sub(r'[^a-z]', ' ', re.sub("’", '', sentence))
        return sentence

    def tokenization(self, sentence):
        """
        Split the sentence into list of token.

        :param sentence: sentence
        :return: list of sentence
        """
        return sentence.split()

    def stopword_removal(self, token):
        """
        Remove stopword in words list using stopword list.

        :param token: list of words
        :return: token that not in stopword list
        """
        temp = []
        for i in range(len(token)):
            if token[i] not in self.stopwords:
                temp.append(token[i])
        return temp

    def stemming(self, tokens):
        for i in range(len(tokens)):
            tokens[i] = self.stemmer.stem(tokens[i])
        return tokens