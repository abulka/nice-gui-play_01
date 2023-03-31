from nicegui import ui

# horizontal splitter demo

# with ui.splitter(horizontal=True).classes('h-96') as splitter:
with ui.splitter(horizontal=True).classes('h-screen') as splitter:
    with splitter.before:
        ui.label('This is some content on the TOP side.'*150)
    with splitter.after:
        ui.label('This is some content on the BOTTOM side.'*150)

ui.run()
