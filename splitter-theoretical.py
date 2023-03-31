from nicegui import ui

with ui.splitter(horizontal=False) as splitter:
    with splitter.add_slot('before'):
        ui.label('This is some content on the left hand side.')
    with splitter.add_slot('after'):
        ui.label('This is some content on the right hand side.')
