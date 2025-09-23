import argparse

class Parser:
    def create_parser(self):
        PARSER = argparse.ArgumentParser()
        PARSER.add_argument("-d", "--directory", metavar="DIRECTORY", help="the directory from output file.")
        PARSER.parse_args()
        return PARSER