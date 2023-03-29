from nicegui import ui
from nicegui.events import ValueChangeEventArguments

# @ui.page('/fred')
# def fred():
#     with ui.header().classes('bg-red-100'):
#         ui.label('Header')
#     with ui.left_drawer(): # overlay=True, , separator=True, fixed=True
#         ui.label('Left drawer')
#     with ui.right_drawer():
#         ui.label('Right drawer')
#     with ui.footer():
#         ui.label('Footer')
#         ui.link('Back to main page', '/#page')

@ui.page('/page_layout')
async def page_layout():
    ui.label('CONTENT')
    [ui.label(f'Line {i}') for i in range(100)]
    with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
        ui.label('HEADER')
        ui.button(on_click=lambda: right_drawer.toggle()).props('flat color=white icon=menu')
    with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
        ui.label('LEFT DRAWER')
    with ui.right_drawer(fixed=False).style('background-color: #ebf1fa').props('bordered') as right_drawer:
        ui.label('RIGHT DRAWER')
    with ui.footer().style('background-color: #3874c8'):
        ui.label('FOOTER')

@ui.page('/other_page')
def other_page():
    ui.label('Welcome to the other side')
    ui.link('Back to main page', '/#page')

@ui.page('/dark_page', dark=True)
def dark_page():
    ui.label('Welcome to the dark side')
    ui.link('Back to main page', '/#page')

# ui.link('Visit fred', fred)
ui.link('Visit page layout', page_layout)
ui.link('Visit other page', other_page)
ui.link('Visit dark page', dark_page)

ui.run(native=True, dark=True)
