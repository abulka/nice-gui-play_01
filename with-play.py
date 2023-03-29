class ParentClass:
    def __init__(self, arg):
        self.arg = arg
        self.collection = []

    def __enter__(self):
        print("Entering context...")
        return self # return self to be assigned to c, the 'as c' part

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context...")

    def do_something(self):
        print(f"Doing something with {self.arg}")

    # add method to add to collection
    def add_to_collection(self, item):
        self.collection.append(item)

class ChildClass:
    pass

with ParentClass("foo") as c:
    c.add_to_collection(ChildClass())

with ParentClass("bar"):
    add_to_collection(ChildClass())

print('c.collection:', c.collection)

