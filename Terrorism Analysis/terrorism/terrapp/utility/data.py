import pandas as pd
import os

class Data():
    # remember the path of this file is the path of workspace so we need to give complete path to the file
    # os.getcwd()
    path = os.path.join(os.path.dirname("__file__"), 'terrapp', 'utility', 'India_1998_JK_DJ.csv')
    data = pd.read_csv(path)
    def __init__(self):
        self.columns = self.data.columns

    def choices(self, col):
            choice = tuple(zip(((self.data)[col].unique()).tolist(), ((self.data)[col].unique()).tolist()))
            return choice

