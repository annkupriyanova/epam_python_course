import os
import sys
import fcntl
import time


class pidfile:
    def __init__(self, file_name):
        self.file = open(file_name, 'w+')
        try:
            fcntl.flock(self.file, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except IOError:
            print('More than one program is forbidden!')
            sys.exit(1)

    def __enter__(self):
        self.file.write(str(os.getpid()))

    def __exit__(self, *exc_info):
        self.file.close()


# def test():
#     filename = 'file1.txt'
#     with pidfile(filename):
#         time.sleep(60)
#
#
# if __name__ == '__main__':
#     test()
