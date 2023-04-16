from nicegui import ui


with ui.column().classes('w-full items-center'):
    ui.label('ANDY2 third had shades mood apart heralds heavenly thy where. Heal olden below who finds monastic and had from vexed,.').classes('text-4xl m-3')
    ui.label('Ernsten ich bilder was früh fühlt. Weiten mit ach folgt die vom, folgt der schauer sich mein welt mit den.Extract images from video').classes('text-3xl m-3')
    label1 = ui.label('HI THERE').style('color: #6E93D6; font-size: 200%; font-weight: 300')
    with ui.card().classes('w-2/3 items-center'):
        ui.label('Card content')
        ui.button('Add label', on_click=lambda: ui.label('Click!'))
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

def update():
    grid.options['rowData'][0]['age'] += 1
    grid.update()

ui.button('Update', on_click=update)
ui.button('Select all', on_click=lambda: grid.call_api_method('selectAll'))

ui.run()
