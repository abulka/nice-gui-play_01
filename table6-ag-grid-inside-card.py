from nicegui import ui

# If you put some other elements in the card, then the card widens and you can see the aggrid. 
# Or just style the card to be forced wider:
# https://github.com/zauberzeug/nicegui/discussions/521

with ui.card().classes('w-2/3 items-center'):
# with ui.card():
    # ui.label('Card content')
    # ui.button('Add label', on_click=lambda: ui.label('Click!'))
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

ui.run()
