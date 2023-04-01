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

with ui.splitter().classes('h-screen') as splitter:
    with splitter.before:
        with ui.splitter(horizontal=True, value=10) as splitter2:
            with splitter2.before:
                ui.label('BRANCHES '*150)
            with splitter2.after:
                with ui.splitter(horizontal=True, value=40) as splitter2:
                    with splitter2.before:
                        with ui.table(title='Commits', columns=columns, rows=rows, selection='single', pagination=10).classes('w-full') as table:
                            with table.add_slot('top-right'):
                                with ui.input(placeholder='Search').props('type=search').bind_value(table, 'filter').add_slot('append'):
                                    ui.icon('search')
                    with splitter2.after:
                        with ui.splitter(horizontal=True) as splitter3:
                            with splitter3.before:
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

                            with splitter3.after:
                                ui.label('DIFFS '*150)
    with splitter.after:
        ui.label('FILE CONTENT '*850)

ui.run(dark=True)

