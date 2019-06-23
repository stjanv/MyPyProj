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
    ok = []
    banned = []

    @staticmethod
    def next_proxy():
        if ProxyServer.ok:
            return ProxyServer.ok.pop(0)
        else:
            if ProxyServer.banned:
                return ProxyServer.banned.pop(0)
            else:
                return 'ProxyServer is empty'

    @staticmethod
    def back_proxy(proxy):
        proxy.used_count += 1
        proxy.used_time = datetime.now()
        if proxy.status == 'Ok':
            ProxyServer.ok.append(proxy)
        elif proxy.status == 'baned':
            ProxyServer.banned.append(proxy)


with open('./ip_list.txt', 'r', encoding='utf-8') as file:
    ip_list = [line.strip() for line in file]
    for i in range(len(ip_list)):
        t = tuple(item for item in ip_list[i].split(':'))
        proxy = Proxy(t[0], t[1])
        ProxyServer.ok.append(proxy)
    file.close()

proxy_to_use = ProxyServer.next_proxy()
print(proxy_to_use)
proxy = Proxy("192.168.0.1","3312")
ProxyServer.back_proxy(proxy)
print(ProxyServer.ok[len(ProxyServer.ok) - 1])

