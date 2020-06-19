from collections import defaultdict
import csv


def get_row_count():
    with open('data.csv', encoding="CP866", newline='', errors='ignore') as csv_in_file:
        row_count = sum(1 for line in csv_in_file) - 1
    return row_count


def get_data_and_line_count():
    columns = defaultdict(list)  # each value in each column is appended to a list

    with open('data.csv', encoding="CP866", newline='', errors='ignore') as csv_in_file:
        reader = csv.DictReader(csv_in_file, delimiter=';')  # read rows into a dictionary format
        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            for (k, v) in row.items():  # go over each column name and value
                columns[k].append(v)  # append the value into the appropriate list
                # based on column name k
    line_count = -1
    for key in columns:
        line_count = line_count + 1
    return columns, line_count


def write_dict_to_csv(data_dict):
    zd = zip(*data_dict.values())
    with open('output.csv', 'w') as csv_out_file:
        writer = csv.writer(csv_out_file, delimiter=';')
        writer.writerow(data_dict.keys())
        writer.writerows(zd)
