from pprint import pprint
from inspect import getmembers
from types import FunctionType

def dump_obj(obj, indent=0):
    if not hasattr(obj, '__dict__') and not isinstance(obj, list):
        print(' ' * indent + str(obj))
        return
    if isinstance(obj, list):
        if not obj:
            print(' ' * indent + '[]')
            return
        print(' ' * indent + '[')
        for item in obj:
            dump_obj(item, indent=indent+2)
        print(' ' * indent + ']')
    else:
        attrs = [a for a in vars(obj) if not a.startswith('_') and a != 'parent' and a != 'parent_slot' and a != 'client']
        if not attrs:
            return
        print(' ' * indent + obj.__class__.__name__ + ':')
        for attr in attrs:
            val = getattr(obj, attr)
            print(' ' * (indent+2) + attr + ':', end=' ')
            dump_obj(val, indent=indent+2)


if __name__ == '__main__':
    class A:
        def __init__(self) -> None:
            self.fred = 1
            self.barney = 2
            self.b = 3
            self.parent = None
            self.children = []
    class B:
        def __init__(self) -> None:
            self.bb1 = 100
            self.bb2 = ['hi']
    a = A()
    a.b = B()
    a.children.append(A())
    dump_obj(a)
