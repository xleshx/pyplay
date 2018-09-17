from setuptools import setup

setup(
    name='worddist',
    entry_points={
        'console_scripts': [
            'wdist = worddistcount:main',
        ],
    }
)