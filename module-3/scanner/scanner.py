from module import *

class Scanner:
    def __init__(self, NETWORK, SUBNET):
        self.NETWORK = NETWORK
        self.SUBNET = SUBNET
        self.IP_LIST = []
        self.targets = []
        self.STATUS = ""
        self.create_list_from_ip()
        self.list_ip_address()

    def create_list_from_ip(self):
        self.IP_LIST = list(ipaddress.ip_network(f"{self.NETWORK}/{self.SUBNET}"))

    def list_ip_address(self):
        self.IP_LIST.pop(0)
        for ip in self.IP_LIST:
            self.ping_hosts(str(ip))

    def ping_hosts(self, IP):
        self.status = ping(IP, verbose=False)
        if self.status.success():
            self.targets.append(IP)
    
    def extract_as_csv(self, data):
        with open("network.csv", "w+") as file:
            header = ["IP", "Status"]
            writer = csv.DictWriter(file, header)
            writer.writeheader()

            for ip in data:
                writer.writerow({"IP": ip, "Status": "Online"})
