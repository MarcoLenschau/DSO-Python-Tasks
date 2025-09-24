from pythonping import ping
import ipaddress, csv

class Scanner:
    def __init__(self, **kargs):
        self.network = kargs.get("network")
        self.subnet = kargs.get("subnet")
        self.filename = kargs.get("filename")
        self.ip_list = []
        self.__targets = []
        self.status = ""
        self.create_list_from_ip()
        self.list_ip_address()
        self.extract_as_csv()

    def get_targets(self):
        return self.__targets
    
    def create_list_from_ip(self):
        self.ip_list = list(ipaddress.ip_network(f"{self.network}/{self.subnet}"))

    def list_ip_address(self):
        self.ip_list.pop(0)
        for ip in self.ip_list:
            self.ping_hosts(str(ip))

    def ping_hosts(self, ip):
        self.status = ping(ip, verbose=False)
        if self.status.success():
            self.__targets.append(ip)
    
    def extract_as_csv(self):
        with open(self.filename, "w+") as file:
            header = ["IP", "Status"]
            writer = csv.DictWriter(file, header)
            writer.writeheader()

            for ip in self.__targets:
                writer.writerow({"IP": ip, "Status": "Online"})
