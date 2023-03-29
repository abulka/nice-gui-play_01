from nicegui import ui

ui.add_head_html('<style>body {background-color: #81D4FA; }</style>')
ui.label('Hello from PyInstaller')
print("HI")

#ui.run(reload=False)
ui.run(reload=False, native=True)
