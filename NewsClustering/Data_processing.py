import pickle
import csv
import os


def load_data(loc):
    """
    Load data from pickle extension to list

    :param loc: location of the pickle extension
    :return: list of dictionary
    """

    with open(os.path.join(os.getcwd(), 'Dataset/' + loc), 'rb') as f:
        data = pickle.load(f)
    return data


def save2csv(loc, data):
    """
    Save list to csv

    :param loc: location of the data that will be saved
    :param data: the data that will be saved
    :return: File csv

    """

    with open(os.path.join(os.getcwd(), 'Model/' + loc), 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)
