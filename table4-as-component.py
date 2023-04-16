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

ui.add_head_html('''
<style>
.my-menu-link {
  color: white;
  background: #59aef2; /* blue */
}
</style>
''')
section_classes = 'w-40 border-l-2 border-gray-300 pl-5'

with ui.element('q-list').props('dense bordered separator'):
    with ui.element('q-item').props('clickable active-class="my-menu-link"').on('click', lambda: click(item1)) as item1:
        with ui.element('q-item-section').props('avatar'):
            ui.element('q-avatar').props('icon=home')
        with ui.element('q-item-section').classes(section_classes):
            ui.label('Hello World!')
        with ui.element('q-item-section').classes(section_classes):
            ui.label('WORLD!')
    with ui.element('q-item').props('clickable active-class="my-menu-link"').on('click', lambda: click(item2)) as item2:
        with ui.element('q-item-section').props('avatar'):
            ui.element('q-avatar').props('icon=bluetooth')
        with ui.element('q-item-section').classes(section_classes):
            ui.label('Bluetooth')
        with ui.element('q-item-section').classes(section_classes):
            ui.label('HA HA')
    with ui.element('q-item').props('clickable active-class="my-menu-link"').on('click', lambda: click(item3)) as item3:
        with ui.element('q-item-section').props('avatar'):
            ui.element('q-avatar').props('icon=wifi')
        # add a left border to the section and some padding
        with ui.element('q-item-section').classes(section_classes):
            ui.label('WiFi')
        with ui.element('q-item-section').classes(section_classes):
            ui.label('HO HOOOOOO')

    items = [
        {'label': 'XHello World!', 'subtitle': 'WORLD!'},
        {'label': 'XBluetooth', 'subtitle': 'HA HA'},
        {'label': 'XWiFi', 'subtitle': 'HO HOOOOOO'},
    ]
    item_elems = []
    for item in items:
        # with ui.element('q-item').props('clickable active-class="my-menu-link"').on('click', lambda: click(item_elem)) as item_elem:
        # with ui.element('q-item').props('clickable active-class="my-menu-link"').on('click', lambda item_elem=item_elem: click(item_elem)) as item_elem:
        # with ui.element('q-item').props('clickable active-class="my-menu-link"').on('click', lambda item_elem=item: click(item_elem)) as item_elem:
        # with ui.element('q-item').props('clickable active-class="my-menu-link"').on('click', lambda x=item_elem: click(x)) as item_elem:
        item_elem = ui.element('q-item')
        print('item_elem', item_elem)
        # with item_elem.props('clickable active-class="my-menu-link"').on('click', lambda: click(item_elem)):
        with item_elem.props('clickable active-class="my-menu-link"').on('click', lambda x=item_elem: print(item_elem, x)):
            """
            How to get the item_elem object in the click handler?
            item_elem is always the same, and x, whilst different, is not an instance of nicegui.element.Element ?!

            <nicegui.element.Element object at 0x10dbc8790> {'id': 26, 'listener_id': '5ac91946-5972-4f68-8b86-593d1961be06', 'args': {'isTrusted': True, '_vts': 1681647441789}}
            <nicegui.element.Element object at 0x10dbc8790> {'id': 33, 'listener_id': '03f7aab0-7365-4240-ace8-a4a0da083ffc', 'args': {'isTrusted': True, '_vts': 1681647443045}}
            <nicegui.element.Element object at 0x10dbc8790> {'id': 40, 'listener_id': '6516bd00-ca31-4872-a475-eb38f8f7a88e', 'args': {'isTrusted': True, '_vts': 1681647444062}}

            """
            with ui.element('q-item-section').props('avatar'):
                ui.element('q-avatar').props('icon=home')
            with ui.element('q-item-section').classes(section_classes):
                ui.label(item['label'])
            with ui.element('q-item-section').classes(section_classes):
                ui.label(item['subtitle'])
        item_elems.append(item_elem)
    print('item_elems', item_elems)

def click(item: ui.element) -> None:
    print('clicked on', item)
    # make all items inactive then activate the one clicked
    for _item in [item1, item2, item3] + item_elems:
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

