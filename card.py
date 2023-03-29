from nicegui import ui

# row with one label
# with ui.row().props('justify-center items-center'):
with ui.column().classes('w-full items-center'):
# with ui.row().classes('w-full items-center'):
    # red bold label
    ui.label('Welcome Andy').style('color: red; font-weight: bold;')

with ui.column().classes('w-full items-center'):
    ui.label('Extract images from video').classes('text-4xl m-3')
    ui.label('Extract images from video').classes('text-3xl m-3')
    label1 = ui.label('HI THERE').style('color: #6E93D6; font-size: 200%; font-weight: 300')

    with ui.card().classes('w-2/3 items-center'):
        ui.label('Card content')
        ui.button('Add label', on_click=lambda: ui.label('Click!'))
        ui.timer(2.0, lambda: ui.label('Tick!'), once=True)

        with ui.card():
            ui.label('Card content2')
            ui.button('Add label2', on_click=lambda: ui.label('Click2!'))
            ui.timer(3.0, lambda: ui.label('Tick22!'), once=True)

# 

button1 = ui.button('Click me!', on_click=lambda: ui.notify(f'You clicked me!'))
button1.props('align=right')
def onclick():
    ui.notify('You clicked me2!')
ui.button('Click me2!', on_click=onclick)

with ui.card():
    class Model:
        def __init__(self):
            self._value = 1
        @property
        def value(self):
            return self._value
        @value.setter
        def value(self, value):
            self._value = value
            ui.notify(f'Value changed to {value}')
        @property
        def value_verbose(self):
            return f'Value is {self._value}'

    model = Model()
    label1 = ui.label('Card content').bind_text_from(model, 'value_verbose')
    label1.style('color: #6E93D6; font-size: 200%; font-weight: 300')
    label1 = ui.label('Card content').bind_text_from(label1, 'text')
    toggle1 = ui.toggle([1, 2, 3], value=1).bind_value(model, 'value')
    toggle2 = ui.toggle({1: 'A', 2: 'B', 3: 'C'}).bind_value(model, 'value')

ui.run(dark=True)
