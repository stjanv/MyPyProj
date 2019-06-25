class Bug(Exception):
    def __init__(self, do):
        self.do = do

    @staticmethod
    def write_to_log(e0):
        with open('log_errors.txt', 'a', encoding='utf-8') as f:
            f.write(f'BugError : {e0} \n')


try:
    raise Bug('face to face')
except Bug as e0:
    Bug.write_to_log(e0)

try:
    raise Bug('face to ass')
except Bug as e0:
    Bug.write_to_log(e0)
