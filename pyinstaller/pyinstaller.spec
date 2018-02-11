# -*- mode: python -*-
# -*- coding: utf-8 -*-

"""
This is a PyInstaller spec file.
"""

import os
from PyInstaller.building.api import PYZ, EXE, COLLECT
from PyInstaller.building.build_main import Analysis
from PyInstaller.utils.hooks import is_module_satisfies

# Constants
DEBUG = os.environ.get("CEFPYTHON_PYINSTALLER_DEBUG", False)

# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

cipher_obj = None


a = Analysis(
    ["../viewer/app.py"],
    pathex=['C:/Program Files (x86)/Windows Kits/10/Redist/ucrt/DLLs/x64'],
    datas=[( '../viewer/views/*.qml', 'views/'),
            ( '../example_files/data.db', '')],
    cipher=cipher_obj,
    win_private_assemblies=True,
    win_no_prefer_redirects=True,
)

pyz = PYZ(a.pure,
          a.zipped_data,
          cipher=cipher_obj)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name="app",
          debug=DEBUG,
          strip=False,
          upx=False,
          console=DEBUG,
          icon="")

COLLECT(exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=False,
        name="app")
