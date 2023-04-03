from pprint import pprint
from inspect import getmembers
from types import FunctionType

def print_obj_structure_OLD(obj, level=0):
    # """Prints the structure of a Python object recursively."""
    # if level == 0:
    #     print(type(obj).__name__)
    # if isinstance(obj, dict):
    #     for k, v in obj.items():
    #         if not k.startswith("_"):
    #             print(" "*(level+2) + f"{k}: ", end="")
    #             print_obj_structure(v, level=level+2)
    # elif isinstance(obj, (list, tuple)):
    #     for i, v in enumerate(obj):
    #         print(" "*(level+2) + f"[{i}]: ", end="")
    #         print_obj_structure(v, level=level+2)
    # elif hasattr(obj, "__dict__"):
    #     for k, v in obj.__dict__.items():
    #         if not k.startswith("_"):
    #             print(" "*(level+2) + f"{k}: ", end="\n")
    #             print_obj_structure(v, level=level+2)
    
    # for attr in dir(obj):
    #     print("obj.%s = %r" % (attr, getattr(obj, attr)))

    
    # def attributes(obj):
    #     disallowed_names = {
    #       name for name, value in getmembers(type(obj)) 
    #         if isinstance(value, FunctionType)}
    #     return {
    #       name for name in dir(obj) 
    #         if name[0] != '_' and name not in disallowed_names and hasattr(obj, name)}
    # pprint(attributes(obj))


    # def attributes(obj, max_depth=1, level=0):
    #     for name, value in getmembers(type(obj)):
    #         print('----', name, value)
                                    
    #     disallowed_names = {
    #         name for name, value in getmembers(type(obj)) 
    #         if isinstance(value, FunctionType)
    #         # exclude names that start with underscore
    #         or name.startswith('_')
    #         # exclude names that start with double underscore
    #         or name.startswith('__')
    #         # exclude 'parent'
    #         or name == 'parent'
    #     }
    #     print(disallowed_names)
    #     result = {}
    #     for name in dir(obj):
    #         if name[0] != '_' and name not in disallowed_names and hasattr(obj, name):
    #             value = getattr(obj, name)
    #             if level < max_depth and not isinstance(value, (int, float)):
    #                 result[name] = attributes(value, max_depth=max_depth, level=level+1)
    #             else:
    #                 result[name] = value
    #     return result

    # pprint(attributes(obj, max_depth=1), indent=4, width=20, depth=5)

    def dump_obj(obj, indent=0):
        if not hasattr(obj, '__dict__') and not isinstance(obj, list):
            print(str(obj))
            return
        print()
        if isinstance(obj, list):
            for item in obj:
                dump_obj(item, indent=indent)
        else:
            attrs = [a for a in vars(obj) if not a.startswith('_') and a != 'parent' and a != 'parent_slot' and a != 'client']
            if not attrs:
                return
            print(' ' * indent + obj.__class__.__name__ + ':')
            for attr in attrs:
                val = getattr(obj, attr)
                print(' ' * (indent+2) + attr + ':', end=' ')
                dump_obj(val, indent=indent+2)
            #     if isinstance(val, list):
            #         for item in obj:
            #             dump_obj(item, indent=indent)
            #     else:
            #         if hasattr(val, '__dict__'):
            #             print()
            #             dump_obj(val, indent=indent+4)
            #         else:
            #             print(val, 'no dict', type(val), hasattr(val, '__dict__'))

    dump_obj(obj)


# def print_obj_structure(obj, level=0):
#     def dump_obj(obj, indent=0):
#         if not hasattr(obj, '__dict__') and not isinstance(obj, list):
#             print(' ' * indent + str(obj))
#             return
#         print()
#         if isinstance(obj, list):
#             for item in obj:
#                 dump_obj(item, indent=indent)
#         else:
#             attrs = [a for a in vars(obj) if not a.startswith('_') and a != 'parent' and a != 'parent_slot' and a != 'client']
#             if not attrs:
#                 return
#             print(' ' * indent + obj.__class__.__name__ + ':')
#             for attr in attrs:
#                 val = getattr(obj, attr)
#                 print(' ' * (indent+2) + attr + ':', end=' ')
#                 if isinstance(val, list):
#                     print()
#                     for item in val:
#                         dump_obj(item, indent=indent+4)
#                 elif hasattr(val, '__dict__'):
#                     print()
#                     dump_obj(val, indent=indent+4)
#                 else:
#                     print(val)

#     dump_obj(obj)

# def print_obj_structure(obj, level=0):
#     def dump_obj(obj, indent=0):
#         if not hasattr(obj, '__dict__') and not isinstance(obj, list):
#             print(str(obj))
#             return
#         if isinstance(obj, list):
#             for item in obj:
#                 dump_obj(item, indent=indent)
#         else:
#             attrs = [a for a in vars(obj) if not a.startswith('_') and a != 'parent' and a != 'parent_slot' and a != 'client']
#             if not attrs:
#                 return
#             print(' ' * indent + obj.__class__.__name__ + ':')
#             for attr in attrs:
#                 val = getattr(obj, attr)
#                 print(' ' * (indent+2) + attr + ':', end=' ')
#                 dump_obj(val, indent=indent+2)
#             print()
#     dump_obj(obj)

# def print_obj_structure(obj, level=0):
#     def dump_obj(obj, indent=0):
#         if not hasattr(obj, '__dict__') and not isinstance(obj, list):
#             print(str(obj))
#             return
#         print()
#         if isinstance(obj, list):
#             print(' ' * indent + '[')
#             for i, item in enumerate(obj):
#                 dump_obj(item, indent=indent+2)
#                 if i < len(obj)-1:
#                     print()
#             print(' ' * indent + ']')
#         else:
#             attrs = [a for a in vars(obj) if not a.startswith('_') and a != 'parent' and a != 'parent_slot' and a != 'client']
#             if not attrs:
#                 return
#             print(' ' * indent + obj.__class__.__name__ + ':')
#             for attr in attrs:
#                 val = getattr(obj, attr)
#                 print(' ' * (indent+2) + attr + ':', end=' ')
#                 dump_obj(val, indent=indent+2)
#     dump_obj(obj)

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
            self.betty = 3
            self.parent = None
            self.children = []

    a = A()
    a.betty = A()
    a.children.append(A())
    # print_obj_structure(a)
    dump_obj(a)
