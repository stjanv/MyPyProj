from datetime import datetime


class Proxy(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.used_time = None
        self.status = 'Ok'
        self.used_count = 0


class ProxyServer(object):
    ok = []
    banned = []

    def next_proxy(self):
        if self.ok != []:
            return self.ok.pop(self.ok[0])
        else:
            if self.banned != []:
                return self.banned.pop(self.banned[0])
            else:
                return 'ProxyServer is empty'

    def back_proxy(self, proxy: Proxy):
        proxy.used_count += 1
        proxy.used_time = datetime.now()
        if proxy.status == 'Ok':
            self.ok.append(Proxy)
        elif proxy.status == 'baned':
            self.banned.append(proxy)


with open('./ip_list.txt', 'r', encoding='utf-8') as file:
    ip_list = [line.strip() for line in file]
    for i in range(len(ip_list)):
        t = tuple(item for item in ip_list[i].split(':'))
        proxy = Proxy(t[0], t[1])
        ProxyServer.ok.append(proxy)