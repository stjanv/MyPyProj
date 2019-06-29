from datetime import datetime


class Proxy(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.used_time = None
        self.status = 'Ok'
        self.used_count = 0

    def __str__(self):
        return f"ip = {self.ip}, port = {self.port}"


class ProxyServer(object):
    def __init__(self):
        self.ok = []
        self.banned = []

    def open_ip_list(self,f):
        with open(f, 'r', encoding='utf-8') as file:
            ip_list = [line.strip() for line in file]
            for i in range(len(ip_list)):
                t = tuple(item for item in ip_list[i].split(':'))
                proxy = Proxy(t[0], t[1])
                self.ok.append(proxy)
            file.close()


    def next_proxy(self):
        if self.ok:
            return self.ok.pop(0)
        else:
            if self.banned:
                return self.banned.pop(0)
            else:
                return 'ProxyServer is empty'


    def back_proxy(self, proxy):
        proxy.used_count += 1
        proxy.used_time = datetime.now()
        if proxy.status == 'Ok':
            self.ok.append(proxy)
        elif proxy.status == 'baned':
            self.banned.append(proxy)






