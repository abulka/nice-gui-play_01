import time
from nicegui import ui


columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True},
    {'name': 'age', 'label': 'Age', 'field': 'age', 'sortable': True},
]
rows = [
    {'id': 0, 'name': 'Alice', 'age': 18},
    {'id': 1, 'name': 'Bob', 'age': 21},
    {'id': 2, 'name': 'Lionel', 'age': 19},
    {'id': 3, 'name': 'Michael', 'age': 32},
    {'id': 4, 'name': 'Julie', 'age': 12},
    {'id': 5, 'name': 'Livia', 'age': 25},
    {'id': 6, 'name': 'Carol'},
]
with ui.table(title='My Team', columns=columns, rows=rows, pagination=5, on_select=lambda e: ui.notify(e.value)).classes('w-96') as table:
# with ui.table(title='My Team', columns=columns, rows=rows, selection='single', pagination=5).classes('w-96') as table:
    # with table.add_slot('top-right'):
    #     with ui.input(placeholder='Search').props('type=search').bind_value(table, 'filter').add_slot('append'):
    #         ui.icon('search')
    # with table.add_slot('bottom-row'):
    #     with table.row():
    #         with table.cell():
    #             ui.button(on_click=lambda: (
    #                 table.add_rows({'id': time.time(), 'name': new_name.value, 'age': new_age.value}),
    #                 new_name.set_value(None),
    #                 new_age.set_value(None),
    #             )).props('flat fab-mini icon=add')
    #         with table.cell():
    #             new_name = ui.input('Name')
    #         with table.cell():
    #             new_age = ui.number('Age')
    pass

ui.label().bind_text_from(table, 'selected', lambda val: f'Current selection: {val}')
ui.button(on_click=lambda: (
        table.add_rows({'name': time.time(), 'age': 100}),
        )).props('flat fab-mini icon=add')
ui.button('Remove', on_click=lambda: table.remove_rows(*table.selected)) \
    .bind_visibility_from(table, 'selected', backward=lambda val: bool(val))
# add 20 rows
for i in range(20):
    table.add_rows({'name': f"{i} {time.time()}", 'age': 100})
# table.on_select=lambda e: ui.notify(e.value)

# with ui.column():
#     ui.label('label 1')
#     ui.label('label 2')
#     ui.label('label 3')

#     # columns = [
#     #     {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
#     #     {'name': 'age', 'label': 'Age', 'field': 'age', 'sortable': True},
#     # ]
#     # rows = [
#     #     {'name': 'Alice', 'age': 18},
#     #     {'name': 'Bob', 'age': 21},
#     #     {'name': 'Carol'},
#     # ]

#     # table = ui.table(columns=columns, rows=rows, row_key='name')
#     # # button to add a new row
#     # # ui.button('Add row', on_click=lambda: rows.append({'name': 'Dave', 'age': 25}))
#     # ui.button(on_click=lambda: (
#     #     table.add_rows({'name': time.time(), 'age': 100}),
#     #     )).props('flat fab-mini icon=add')    
#     # # button to print rows
#     # ui.button('Print rows', on_click=lambda: print(rows))
#     # # button to clear table
#     # ui.button('Clear table', on_click=lambda: table.clear())


#     # with ui.table(title='My Team', columns=columns, rows=rows, selection='multiple', pagination=10).classes('w-96') as table:
#     #     # with table.add_slot('bottom-row'):
#     #     #     with table.row():
#     #     #         with table.cell():
#     #     #             ui.button(on_click=lambda: (
#     #     #                 table.add_rows({'name': time.time(), 'age': 100}),
#     #     #                 )).props('flat fab-mini icon=add')    
#     #     with table.add_slot('bottom-row'):
#     #         with table.row():
#     #             with table.cell():
#     #                 ui.button(on_click=lambda: (
#     #                     table.add_rows({'id': time.time(), 'name': new_name.value, 'age': new_age.value}),
#     #                     new_name.set_value(None),
#     #                     new_age.set_value(None),
#     #                 )).props('flat fab-mini icon=add')
#     #             with table.cell():
#     #                 new_name = ui.input('Name')
#     #             with table.cell():
#     #                 new_age = ui.number('Age')

#     # ui.tree([
#     #     {'id': 'numbers', 'children': [{'id': '1'}, {'id': '2'}]},
#     #     {'id': 'letters', 'children': [{'id': 'A'}, {'id': 'B'}]},
#     # ], label_key='id', on_select=lambda e: ui.notify(e.value))
#     ui.tree([
#         {'id': 'numbers', 'children': [{'id': '1'}, {'id': '2'}]},
#         {'id': 'letters', 'children': [{'id': 'A'}, {'id': 'B'}]},
#     ], label_key='id', on_select=lambda e: ui.notify(e.value))

#     ui.tree([
#         {'id': 'numbers', 'children': [{'id': '1'}, {'id': '2'}]},
#         {'id': 'letters', 'children': [{'id': 'A'}, {'id': 'B'}]},
#     ], label_key='id', on_select=lambda e: ui.notify(e.value))

#     # ui.tree([
#     #     {
#     #         'label': 'Satisfied customers (with avatar)',
#     #         'avatar': 'https://cdn.quasar.dev/img/boy-avatar.png',
#     #         'children': [
#     #             {
#     #                 'label': 'Good food (with icon)',
#     #                 'icon': 'restaurant_menu',
#     #                 'children': [
#     #                     {'label': 'Quality ingredients'},
#     #                     {'label': 'Good recipe'}
#     #                 ]
#     #             },
#     #             {
#     #                 'label': 'Good service (disabled node with icon)',
#     #                 'icon': 'room_service',
#     #                 'disabled': True,
#     #                 'children': [
#     #                     {'label': 'Prompt attention'},
#     #                     {'label': 'Professional waiter'}
#     #                 ]
#     #             },
#     #             {
#     #                 'label': 'Pleasant surroundings (with icon)',
#     #                 'icon': 'photo',
#     #                 'children': [
#     #                     {
#     #                         'label': 'Happy atmosphere (with image)',
#     #                         'img': 'https://cdn.quasar.dev/img/logo_calendar_128px.png'
#     #                     },
#     #                     {'label': 'Good table presentation'},
#     #                     {'label': 'Pleasing decor'}
#     #                 ]
#     #             }
#     #         ]
#     #     }
#     # ], label_key='label', on_select=lambda e: ui.notify(e.value))

#     with ui.row():
#         ui.label('label 4')
#         ui.label('label 5')
#         ui.label('label 6')





# # https://github.com/zauberzeug/nicegui/blob/9f955f90c5c5a903894c27e60a8bd5cda46634f2/tests/test_table.py


# def columns(): return [
#     {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True},
#     {'name': 'age', 'label': 'Age', 'field': 'age', 'sortable': True},
# ]


# def rows(): return [
#     {'id': 0, 'name': 'Alice', 'age': 18},
#     {'id': 1, 'name': 'Bob', 'age': 21},
#     {'id': 2, 'name': 'Lionel', 'age': 19},
# ]

# with ui.table(columns=columns(), rows=rows()) as table:
#     with table.add_slot('top-row'):
#         with table.row():
#             with table.cell():
#                 ui.label('This is the top slot.')
#     table.add_slot('body', '''
#         <q-tr :props="props">
#             <q-td key="name" :props="props">overridden</q-td>
#             <q-td key="age" :props="props">
#                 <q-badge color="green">{{ props.row.age }}</q-badge>
#             </q-td>
#         </q-tr>
#     ''')
    
ui.run(dark=True)
