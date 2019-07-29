from Preprocessing.Preprocessing import Preprocessing
from NewsSummarizer.Summarizer import word_freq


def fit(documents):

    pre = Preprocessing()

    data = []
    for i in range(len(documents)):
        data.append(pre.stemming(pre.stopword_removal(pre.tokenization(pre.casefolding(documents[i])))))
    data = (list(filter(None, data)))

    wordfreq = word_freq(data)

    ranking = []
    for words in data:
        temp = 0
        for word in words:
            temp += wordfreq[word]
        ranking.append(temp)

    sort_list = sorted(range(len(ranking)), key=ranking.__getitem__, reverse=True)
    n = 3
    doc = ''
    for i in range(n):
        doc += '{}. '.format(documents[sort_list[i]])
    return doc