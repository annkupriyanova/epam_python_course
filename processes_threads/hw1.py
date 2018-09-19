import psutil


def process_count(username):
    return sum([1 for process in psutil.process_iter() if process.username() == username])


def total_memory_usage(root_pid):
    if psutil.pid_exists(root_pid):
        root_process = psutil.Process(pid=root_pid)
        memory_usage = sum([p.memory_info()[0] for p in root_process.children(recursive=True)])
        memory_usage += root_process.memory_info()[0]
        return memory_usage
    else:
        return f'Process with pid {root_pid} is not found.'


if __name__ == '__main__':
    print(process_count('root'))
    print(total_memory_usage(1307))
