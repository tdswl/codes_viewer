from setuptools import setup

setup(
    name='codes_viewer',
    packages=['viewer'],
    include_package_data=True,
    install_requires=[
        'pyexcel',
        'pyexcel-xls',
        'pyqt5'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ]
)
