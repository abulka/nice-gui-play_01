import os
import subprocess
from pathlib import Path
import nicegui

cmd = [
    'pyinstaller',
    'simple.py', # your main file with ui.run()
    '--name', 'myapp', # name of your app
#    '--onefile',
#    '--windowed',
    '--add-data', f'{Path(nicegui.__file__).parent}{os.pathsep}nicegui'       
]
subprocess.call(cmd)

