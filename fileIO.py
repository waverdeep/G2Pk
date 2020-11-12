import csv


def write_csv_file(file_path, dataset):
    f = open(file_path, 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    for item in dataset:
        wr.writerow(item)