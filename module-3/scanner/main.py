from scanner import Scanner
from parser import Parser

if __name__ == "__main__":
    PARSER = Parser().create_parser()
    ARGS = PARSER.parse_args()
    SCANNER = Scanner(network=ARGS.network, subnet=ARGS.subnet, filename=ARGS.csv) 