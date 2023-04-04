from nicegui import ui
from dump_obj import dump_obj

def find_label(element):
    """
    Recursively search for a `Label` object in an element's children.
    Return `None` if not found.
    """
    if isinstance(element, ui.label):
        # Found the `Label` object
        return element

    # Check children recursively
    for child in element.default_slot.children:
        if isinstance(child, ui.element):
            label = find_label(child)
            if label is not None:
                return label

    # `Label` object not found
    return None

section_classes = 'w-40 border-l-2 border-gray-300 pl-5'

with ui.element('q-list').props('dense bordered separator'):
    with ui.element('q-item').props('clickable v-ripple').on('click', lambda: click(item1)) as item1:
        with ui.element('q-item-section').props('avatar'):
            ui.element('q-avatar').props('icon=home')
        with ui.element('q-item-section').classes(section_classes):
            ui.label('Hello World!')
        with ui.element('q-item-section').classes(section_classes):
            ui.label('WORLD!')
    with ui.element('q-item').props('clickable').on('click', lambda: click(item2)) as item2:
        with ui.element('q-item-section').props('avatar'):
            ui.element('q-avatar').props('icon=bluetooth')
        with ui.element('q-item-section').classes(section_classes):
            ui.label('Bluetooth')
        with ui.element('q-item-section').classes(section_classes):
            ui.label('HA HA')
    with ui.element('q-item').props('clickable').on('click', lambda: click(item3)) as item3:
        with ui.element('q-item-section').props('avatar'):
            ui.element('q-avatar').props('icon=wifi')
        # add a left border to the section and some padding
        with ui.element('q-item-section').classes(section_classes):
            ui.label('WiFi')
        with ui.element('q-item-section').classes(section_classes):
            ui.label('HO HOOOOOO')

def click(item: ui.element) -> None:
    # make all items inactive then activate the one clicked
    for _item in [item1, item2, item3]:
        _item._props['active'] = False
        _item.update()
    # activate the one clicked, not by toggling but by setting to True
    item._props['active'] = True
    item.update()

    # find the label in the item and print its text
    label = find_label(item)
    if label is not None:
        ui.notify(label.text)

    # dump_obj(item)

ui.checkbox('hello!', on_change=lambda e: ui.notify(e.value))

ui.run(port=8081)

