from nicegui import ui

with ui.splitter().classes('h-screen') as splitter:
    with splitter.before:
        with ui.splitter(horizontal=True) as splitter2:
            with splitter2.before:
                ui.label('BRANCHES '*150)
            with splitter2.after:
                ui.label('COMMITS '*150)
    with splitter.after:
        ui.label('FILE CONTENT '*150)

ui.run(dark=True)

