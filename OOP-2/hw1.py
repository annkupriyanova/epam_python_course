class EnsurePositive:
    def __init__(self, var_name, init_value=0):
        self.name = var_name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.name] = value
        else:
            print("Can't set negative value.")


class BePositive:
    x = EnsurePositive('x')
    y = 0

    def __init__(self, x0=0, y0=0):
        self.x = x0
        self.y = y0


def test():
    instance = BePositive(5, 7)
    instance2 = BePositive(1, 1)
    print(f'1: x = {instance.x}, y = {instance.y}')
    print(f'2: x = {instance2.x}, y = {instance2.y}')

    instance.x = -12
    instance.y = -10
    instance2.x = 12
    print(f'1: x = {instance.x}, y = {instance.y}')
    print(f'2: x = {instance2.x}, y = {instance2.y}')


if __name__ == '__main__':
    test()
