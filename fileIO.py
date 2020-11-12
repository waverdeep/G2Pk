import csv
import pandas as pd


def write_csv_file(file_path, dataset):
    f = open(file_path, 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    for item in dataset:
        wr.writerow(item)


def read_csv_file(file_path, encoding='utf-8'):
    scripts = []
    f = open(file_path, 'r', encoding=encoding)
    lines = csv.reader(f)
    for line in lines:
        scripts.append(line)
    f.close()
    return scripts


def read_csv_pandas(filepath):
    return pd.read_csv(filepath)