import os
import subprocess
from pathlib import Path
import nicegui

cmd = [
    'pyinstaller',
    # 'main.py', # your main file with ui.run()
    'nice02.py', # your main file with ui.run()
    '--name', 'myapp', # name of your app
    '--onefile',
    '--windowed',
    '--add-data', f'{Path(nicegui.__file__).parent}{os.pathsep}nicegui'       
]
subprocess.call(cmd)
