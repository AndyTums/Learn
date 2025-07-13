import csv


def read_csv(file_path):
    """ Чтение CSV файла """

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)
