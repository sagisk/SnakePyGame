import csv
import pandas as pd

class Model:
    def __init__(self, model_name):
        self.model_name = model_name

    def write_data(self, file_name, row, header = False):
        with open('{}.csv'.format(file_name), mode = 'a+', newline='') as file:
            file_writer = csv.writer(file)
            if header:
                file_writer.writerow(['X', 'Y', 'F_X', 'F_Y'])
            file_writer.writerows(row)
        file.close()

    def read_data(self, file_dir):
        return pd.DataFrame(file_dir)

    def fit(self):
        return None

    def predict(self):
        return None