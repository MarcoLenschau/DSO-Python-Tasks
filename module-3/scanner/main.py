from scanner import Scanner
from parser import Parser

if __name__ == "__main__":
    PARSER = Parser().create_parser()
    ARGS = PARSER.parse_args()
    SCANNER = Scanner(ARGS.network, ARGS.subnet, ARGS.filename)  