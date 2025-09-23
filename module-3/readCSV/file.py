import pandas as pd
import os 

class File:
    def __init__(self, directory):
        self.directory = directory
        self.files = []
        self.check_csv()
        self.read_files()
        if directory is not None:
            print("Please provide a directory containing CSV files using the -d argument.")

    def read(self, file):
        return pd.read_csv(file)
    
    def check_csv(self): 
        for file in os.listdir(self.directory):
            if file.endswith(".csv"):
                self.file = file
                self.files.append(file)

    def read_files(self):
        for file in self.files:
            file = self.read(file)
            print(file)