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

with ui.element('q-list').props('bordered separator'):
    with ui.element('q-item').props('clickable').on('click', lambda: click(item1)) as item1:
        with ui.element('q-item-section'):
            ui.label('Hello World!')
    with ui.element('q-item').props('clickable').on('click', lambda: click(item2)) as item2:
        with ui.element('q-item-section').props('avatar'):
            ui.element('q-avatar').props('icon=bluetooth')
        with ui.element('q-item-section'):
            ui.label('Bluetooth')
    with ui.element('q-item').props('clickable').on('click', lambda: click(item3)) as item3:
        with ui.element('q-item-section').props('avatar'):
            ui.element('q-avatar').props('icon=wifi')
        with ui.element('q-item-section'):
            ui.label('WiFi')

def click(item: ui.element) -> None:
    item._props['active'] = not item._props.get('active', False)
    item.update()
    # ui.notify(item.slots['default'].children[0].slots['default'].children[0].text)
    # keep drilling down till through slots and children till find tag property of 'q-label'

    label = find_label(item)
    if label is not None:
        # ui.notify(label.slots['default'].children[0].text)
        ui.notify(label.text)

    dump_obj(item)

ui.checkbox('hello!', on_change=lambda e: ui.notify(e.value))

ui.run(port=8081)

