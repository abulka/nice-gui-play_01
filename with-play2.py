"""
falkoschindler — Today at 6:53 PM
We're glad you like it, @tcab! By implementing the __enter__ and __exit__
methods of a class you can create define what happens when used with a with
expression. For NiceGUI elements, we pass it down to the default_slot
(https://github.com/zauberzeug/nicegui/blob/main/nicegui/element.py#L67-L72).
Slots are basically 1:1 representations of Vue slots. Thus, child elements are
not directly nested in a parent element, but its default slot. In the slot's
__enter__ and __exit__ method we keep track of the current "context",
represented with a slot stack:
https://github.com/zauberzeug/nicegui/blob/main/nicegui/slot.py#L19-L25. It
tracks the slot you're currently in. Finally, when creating a new element, it
finds it parent slot on the slot stack:
https://github.com/zauberzeug/nicegui/blob/main/nicegui/element.py#L50

write a python class Element which can hold a list of children. Implement the
'with' protocol by implementing the __enter__ and __exit__ methods so that the
class can be use in a 'with' statement e.g. `with Element():`. Keep a
combination of global variables and Element properties so that when each
subclass of Element is created inside a with statement, the Element __init__
method knows who the parent Element is and wires it up accordingly, so that each
element knows its children.
"""


class Element:
    """Example of a class which implements the 'with' protocol and can create a tree
    structure of elements without needing explicit .add_child() calls.
    """
    parent = None

    def __init__(self, name='Untitled'):
        self.children = []
        self.name = name

        if Element.parent:
            Element.parent.children.append(self)

    def __enter__(self):
        Element.parent = self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        Element.parent = self.parent

    def __str__(self, level=0, closing_tags=False):
        indent = "  " * level
        output = f"{indent}<{self.name}>\n"
        for child in self.children:
            output += child.__str__(level + 1)
        if closing_tags:
            output += f"{indent}</{self.name}>\n"
        return output


with Element('Parent') as parent:
    Element('Child 1')
    Element('Child 2')
    with Element('Child 3'):
        Element('Grandchild 1')
        Element('Grandchild 2')

print(parent)
