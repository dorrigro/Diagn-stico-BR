from setuptools import setup

setup(
    name='diagnostico-app',
    version='1.0',
    packages=['src'],
    package_dir={'': 'src'},
    install_requires=[
        'psutil',
        'keyboard',
    ],
    entry_points={
        'console_scripts': [
            'diagnostico=Diagnóstico:main',
        ],
    },
    options={
        'build_exe': {
            'packages': ['psutil', 'keyboard'],
        }
    },
)