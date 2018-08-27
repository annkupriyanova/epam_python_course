import os


class pidfile:
    def __init__(self, file_name):
        if 'file' in self.__dict__ and not self.file.closed:
            raise Exception
        else:
            self.file = open(file_name, 'w')

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