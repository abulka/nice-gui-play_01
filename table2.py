from nicegui import ui

columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
    {'name': 'age', 'label': 'Age', 'field': 'age', 'sortable': True},
]
rows = [
    {'name': 'Alice', 'age': 18},
    {'name': 'Bob', 'age': 21},
    {'name': 'Carol'},
]

# ui.table(columns=columns, rows=rows, row_key='name', on_select=lambda e: print(e.value))
# ui.table(columns=columns, rows=rows, row_key='name', on_select=lambda e: ui.notify(e.value))
ui.table(columns=columns, rows=rows, row_key='name', selection='single', on_select=lambda e: ui.notify(e.value))

ui.checkbox('hello', on_change=lambda e: ui.notify(e.value))

ui.run(port=8081)

