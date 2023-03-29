import os
import subprocess
from pathlib import Path
import nicegui

# ensure you `pip install pyinstaller` first within your venv so that the correct pyinstaller is used
cmd = [
    # 'pyinstaller',
    'python',
    '-m',
    'PyInstaller',
    'main.py', # your main file with ui.run()
    # 'nice02.py', # your main file with ui.run()
    '--name', 'myapp', # name of your app
    '--onefile',
    '--windowed',  # dangerous option cos can't see console output and also cannot stop app with ctrl-c
    '--add-data', f'{Path(nicegui.__file__).parent}{os.pathsep}nicegui'       
]
subprocess.call(cmd)

# python -m PyInstaller main.py --name myapp --hidden-import=nicegui --add-data /Volumes/SSD/Data/Devel/test-projects/nice-gui-01/venv/lib/python3.10/site-packages/nicegui:nicegui