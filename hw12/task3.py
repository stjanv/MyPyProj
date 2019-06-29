from datetime import datetime
import sys

class ContDec(object):
    def __init__(self):
        self.time_to_start = None
        self.time_to_finish = None

    def __call__(self, funk):
        def wrapper():
            self.__enter__()
            exc_type = None
            exc_val = None
            exc_tb = None
            try:
                funk()
            except:
                exc_type, exc_val, exc_tb = sys.exc_info()
            self.__exit__(exc_type, exc_val, exc_tb )
        return wrapper


    def __enter__(self):
        self.time_to_start = datetime.now()
        print(self.time_to_start)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.time_to_finish = datetime.now() - self.time_to_start
        print(self.time_to_finish)




@ContDec()
def read_file():
    with open('rockyou.txt', 'r',encoding='utf-8') as f:
        f.readlines()


read_file()

print('------------------------------------------------')

with ContDec():
    read_file()
