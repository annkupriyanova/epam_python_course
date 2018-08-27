
class EnumMeta(type):
    def __new__(cls, *args, **kwargs):
        # reversed_enum_pairs = {}
        storage = {key: value for key, value in args[2].items() if not key.startswith('__')}

        enum_cls = super().__new__(cls, *args, **kwargs)
        enum_cls.storage = storage
        enum_cls.dict_of_instances = {key: enum_cls(value) for key, value in storage.items()}

        return enum_cls


class Enum(metaclass=EnumMeta):
    def __new__(cls, *args, **kwargs):
        # print(cls.__dict__)
        if args[0] not in cls.storage.values():
            print(f'ValueError: {args[0]} is not a valid parameter')
        else:
            key = next(k for k, v in cls.storage.items() if v == args[0])
            if key in cls.dict_of_instances:
                return cls.dict_of_instances[key]
            else:
                new_instance = super().__new__(cls)
                # new_instance.__class__ = Enum
                new_instance.name = key
                new_instance.value = cls.storage[key]

                return new_instance

    def __str__(self):
        pass

    def __getitem__(self, item):
        if item in self.dict_of_instances:
            return self.dict_of_instances[item]
        else:
            raise KeyError


class Direction(Enum):
    north = 0
    east = 90
    south = 180
    west = 270


def test():
    print(Direction.west)
    Direction(90)
    print(Direction.east)
    print(Direction.dict_of_instances['north'].name)
    print(Direction.dict_of_instances['north'].value)

    print(Direction['west'])


if __name__ == '__main__':
    test()