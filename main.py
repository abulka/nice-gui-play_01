from nicegui import ui

ui.label('Hello from PyInstaller')

# ui.run(reload=False)
ui.run(reload=False, native=True, dark=True)
