from nicegui import ui
# from obj_dumper import print_obj_structure
# from beeprint import pp
from dump_obj import dump_obj

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
    # print_obj_structure(item)
    dump_obj(item)
    # ui.notify(item.slots['default'].children[0].slots['default'].children[0].text)
    # keep drilling down till through slots and children till find tag property of 'q-label'

    # from pprint import pprint
    # pprint(vars(item))

    # pp(item)

    # print(repr(item))

    # attrs_with_value = {attr: getattr(item, attr) for attr in dir(item)}
    # attrs_with_value = {attr: getattr(item, attr) for attr in dir(item) and "__" not in attr}
    # attrs_with_value = {attr: getattr(item, attr) for attr in dir(item) and "__" not in dir(item) and "_" not in dir(item)}
    # print(attrs_with_value)

    # from ppretty import ppretty
    # # print(ppretty(item, indent=4, width=80, depth=5))
    # print(ppretty(item, indent='    ', width=40, seq_length=10, depth=8,
    #           show_protected=False, show_static=True, show_properties=True, show_address=True))

ui.checkbox('hello!', on_change=lambda e: ui.notify(e.value))

ui.run(port=8081)

