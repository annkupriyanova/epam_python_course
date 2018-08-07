def merge_files(fname1: str, fname2: str) -> str:
    try:
        with open(fname1, 'r') as file1:
            with open(fname2, 'r') as file2:
                with open('result_file.txt', 'w+') as result_file:
                    num1 = file1.readline()
                    num2 = file2.readline()
                    while True:
                        if num1 == '':
                            result_file.write('\n' + num2 + file2.read())
                            break
                        if num2 == '':
                            result_file.write('\n' + num1 + file1.read())
                            break

                        if int(num1) < int(num2):
                            result_file.write(num1)
                            num1 = file1.readline()
                        elif int(num1) > int(num2):
                            result_file.write(num2)
                            num2 = file2.readline()
                        else:
                            result_file.write(num1 + num2)
                            num1 = file1.readline()
                            num2 = file2.readline()

        return result_file.name

    except OSError as e:
        print(e.__str__())
        return ''


if __name__ == '__main__':
    print(merge_files('file1.txt', 'file2.txt'))
