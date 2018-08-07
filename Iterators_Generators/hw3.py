import os
import stat
from os.path import isfile, join
from itertools import combinations


def hardlink_check(directory_path: str) -> bool:
    answer = False

    try:
        files = [file for file in os.listdir(directory_path) if isfile(join(directory_path, file))]

        for (f1, f2) in combinations(files, 2):
            if is_hard_link(f1, f2):
                answer = True
                break

    except OSError as e:
        print(e.__str__())

    return answer


def is_hard_link(file1, file2):
    s1 = os.stat(file1)
    s2 = os.stat(file2)
    return s1[stat.ST_INO] == s2[stat.ST_INO]


if __name__ == '__main__':
    print(hardlink_check('./'))
