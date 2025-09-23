import argparse

class Parser:
    def create_parser(self):
        PARSER = argparse.ArgumentParser(description="A simple network scanner.")
        PARSER.add_argument("-s", "--subnet", metavar="SUBNET", help="the subnet as a CIDR suffix.")
        PARSER.add_argument("-n", "--network", metavar="NETWORK", help="the network to be scanned.")
        PARSER.add_argument("-csv", "--csv", metavar="FILENAME", help="the output CSV filename.")
        PARSER.parse_args()
        return PARSER