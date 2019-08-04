import csv
import os
from pathlib import Path


class ReadCsv:
    def __init__(self, path):
        base_path = os.path.dirname(Path(__file__).parent.parent)
        with open(base_path + '/csv_files/' + path) as csv_file:
            csv_dictionary = {}
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    csv_dictionary[row[0]] = row[1]
            print(csv_dictionary)


read = ReadCsv('the_Demo_site/test_data.csv')
