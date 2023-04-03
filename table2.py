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

"""
ui.table is not responding to on_select event #698

https://github.com/zauberzeug/nicegui/issues/698#issuecomment-1493363356

By default ui.table has row selections disabled. You need to pass
selection='single' or selection='multiple' as an argument to activate it.

If you wan't to get click events instead without the need for checkboxes, it is,
unfortunately, currently not possible. There's a related discussion over here:
#664.
"""
# ui.table(columns=columns, rows=rows, row_key='name', on_select=lambda e: print(e.value))
# ui.table(columns=columns, rows=rows, row_key='name', on_select=lambda e: ui.notify(e.value))
tbl = ui.table(columns=columns, rows=rows, row_key='name', selection='single', on_select=lambda e: ui.notify(e.selection))
tbl.props('bordered separator dense')

ui.checkbox('hello', on_change=lambda e: ui.notify(e.value))

ui.run(port=8081)

