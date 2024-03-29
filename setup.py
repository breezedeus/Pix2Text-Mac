"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['pix2text_app.py']
DATA_FILES = [('', ['./config.yaml',],)]
OPTIONS = {
    'iconfile': './icons/p2t.icns',
    'plist': {
        'CFBundleName': 'Pix2Text',  # Application Name
        'CFBundleDisplayName': 'Pix2Text',  # Application Display Name
        'CFBundleVersion': '1.0.2',  # Application version number
        'CFBundleIdentifier': 'Pix2Text',  # Application package name and unique identifier
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
