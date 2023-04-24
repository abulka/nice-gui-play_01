from nicegui import ui
from nicegui.events import ValueChangeEventArguments

with ui.row():
    ui.button('Button', on_click=lambda: ui.notify('Click1'))
    ui.button('Button', on_click=lambda: ui.notify('Click2'))

# add row with a button
with ui.row() as row0:
    btn0 = ui.button('Button', on_click=lambda: ui.notify('Click'))
print(row0, btn0, dir(row0)) # put breakpoint here

# do the same as above without the with ?
row1 = ui.row()
button1 = ui.button('Button Click Manually', on_click=lambda: ui.notify('Click Manually'))
# row1.add_slot(button1) # NO
# row1.default_slot.children.append(button1) # YES?



knob = ui.knob(0.3, show_value=True)
ui.button('turn up', on_click=lambda: knob.set_value(0.8))

# See https://github.com/zauberzeug/nicegui/discussions/804
modifyable_tree = ui.tree([
    {'id': 'numbers', 'children': [
        {'id': '1'}, {'id': '2'}]},
    {'id': 'letters', 'children': [{'id': 'A'}, {'id': 'B'}]},
], label_key='id', on_select=lambda e: ui.notify(e.value))

# add button to add a new item to the tree under letters DOESN'T WORK
ui.button('add item', on_click=lambda: modifyable_tree.nodes.append({'id': 'C'}))

ui.tree([
    {'id': 'numbers', 'children': [
        {'id': '1'}, {'id': '2'}]},
    {'id': 'letters', 'children': [{'id': 'A'}, {'id': 'B'}]},
], label_key='id', on_select=lambda e: ui.notify(e.value))

ui.tree([
    {'id': 'numbers', 'children': [
        {'id': '1', 'children': [
            {'id': '11'},
            {'id': '12', 'children': [
                {'id': '121'},
                {'id': '122'}
            ]}
        ]},
        {'id': '2', 'children': [
            {'id': '21'},
            {'id': '22'}
        ]}
    ]},
    {'id': 'letters', 'children': [
        {'id': 'A', 'children': [
            {'id': 'AA'},
            {'id': 'AB'}
        ]},
        {'id': 'B', 'children': [
            {'id': 'BA'},
            {'id': 'BB'}
        ]}
    ]}
], label_key='id', on_select=lambda e: ui.notify(e.value))

ui.run(native=True, dark=True)
