from nicegui import ui
from nicegui.events import ValueChangeEventArguments

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

ui.add_head_html('<style>body {background-color: #81D4FA; }</style>')
# make it black
# ui.add_head_html('<style>body {background-color: #000; }</style>')

ui.button('Button', on_click=lambda: ui.notify('Click'))
with ui.row():
    ui.checkbox('Checkbox', on_change=show)
    ui.switch('Switch', on_change=show)
ui.radio(['A', 'B', 'C'], value='A', on_change=show).props('inline')
with ui.row():
    ui.input('Text input', on_change=show)
    ui.select(['One', 'Two'], value='One', on_change=show)
ui.link('And many more...', '/documentation').classes('mt-8')

# ui.run()
# ui.run(reload=False)
# ui.run(native=True, dark=True)
ui.run(native=False, dark=True)
# ui.run(reload=False, native=True)
