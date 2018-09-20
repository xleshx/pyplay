from setuptools import setup

setup(
    name='Worddist',
    version='1.0',
    description='Word distance counter',
    author='Alexey Antipov',
    author_email='alexey.lesh@gmail.com',
    url='https://github.com/xleshx/pyplay',
    packages=['worddistcount', 'test'],
    entry_points={
        'console_scripts': [
            'wdist = worddistcount:main',
        ],
    }
)
