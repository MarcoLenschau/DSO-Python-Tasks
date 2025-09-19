from scanner import Scanner

NETWORK = "192.168.13.0"
SUBNET = "28"

if __name__ == "__main__":
    scanner = Scanner(NETWORK, SUBNET)
    targets = scanner.targets   
    scanner.extract_as_csv(targets)