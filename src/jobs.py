from functools import lru_cache
import csv


def create_row_dict(header, row):
    dict_row = dict()
    for index in range(len(row)):
        dict_row[header[index]] = row[index]
    return dict_row


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path, encoding='UTF-8') as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        header, *rows = reader

    data_list = list()
    for row in rows:
        data_list.append(create_row_dict(header, row))

    return data_list
