from nicegui import ui

# this is only a bug if you don't close the other open nicegui windows
# then update the source code and save.

grid = ui.aggrid({
    'columnDefs': [
        {'headerName': 'Name', 'field': 'name'},
        {'headerName': 'Age', 'field': 'age'},
    ],
    'rowData': [
        {'name': 'Alice', 'age': 18},
        {'name': 'Bob', 'age': 21},
        {'name': 'Carol', 'age': 42},
    ],
    'rowSelection': 'multiple',
}).classes('max-h-40')

ui.label('hello4').classes('text-4xl m-3')


ui.run()