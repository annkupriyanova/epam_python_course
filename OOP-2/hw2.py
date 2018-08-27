
class EnumMeta(type):
    def __new__(cls, name, bases, dct):
        storage = {}
        reversed_storage = {}
        enum_list = []

        for key, value in dct.items():
            if not key.startswith('__'):
                storage[key] = value
                reversed_storage[value] = key

        dct['storage'] = storage
        dct['reversed_storage'] = reversed_storage

        enum_cls = super().__new__(cls, name, bases, dct)

        for key, value in dct['storage'].items():
            enum_instance = enum_cls(value)
            enum_list.append(enum_instance)
            setattr(enum_cls, key, enum_instance)

        setattr(enum_cls, '_enum_list', tuple(enum_list))

        return enum_cls

    def __iter__(self):
        return iter(self._enum_list)

    def __getitem__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        else:
            raise KeyError(f'{key}')


class Enum(metaclass=EnumMeta):
    def __new__(cls, value):
        if value not in cls.reversed_storage:
            raise ValueError(f'{value} is not a valid {cls.__name__}')
        else:
            key = cls.reversed_storage[value]
            for enum_instance in cls._enum_list:
                if value == enum_instance.value:
                    return enum_instance

        new_instance = super().__new__(cls)
        new_instance.__class__ = cls
        new_instance.name = key
        new_instance.value = cls.storage[key]

        return new_instance

    def __str__(self):
        return f'{type(self).__name__}.{self.name}'

    def __repr__(self):
        return f'<{type(self).__name__}.{self.name}: {self.value}>'


class Direction(Enum):
    north = 0
    east = 90
    south = 180
    west = 270


# def test():
#     for d in Direction:
#         print(d)
#
#
# if __name__ == '__main__':
#     test()