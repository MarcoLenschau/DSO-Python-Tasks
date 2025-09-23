from file import File
from parser import Parser

if __name__ == "__main__":
    PARSER = Parser().create_parser()
    ARGS = PARSER.parse_args()
    DIRECTORY = ARGS.directory
    FILE = File(DIRECTORY)