import pandas as pd
import os, sys; 

class File:
    def __init__(self, directory):
        self.directory = directory
        self.files = []
        self.check_csv()
        self.read_files()

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


if __name__ == "__main__":
    try:
        f1 = File(sys.argv[1])
    except IndexError as error:
        print(f"{error}")