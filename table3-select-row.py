from nicegui import ui
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
    # ui.notify(item.slots['default'].children[0].slots['default'].children[0].text)
    # keep drilling down till through slots and children till find tag property of 'q-label'
    dump_obj(item)

ui.checkbox('hello!', on_change=lambda e: ui.notify(e.value))

ui.run(port=8081)

