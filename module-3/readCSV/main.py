from file import File
from parser import Parser

if __name__ == "__main__":
    PARSER = Parser().create_parser()
    ARGS = PARSER.parse_args()
    DIRECTORY = ARGS.directory
    if DIRECTORY:
        File(DIRECTORY)
    else:
        print("Please provide a directory containing CSV files using the --directory argument.")