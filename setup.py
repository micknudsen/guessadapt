from setuptools import setup, find_packages

setup(

    name='guessadapt',

    packages=find_packages('src'),
    package_dir={'': 'src'},

    entry_points={
        'console_scripts': ['guessadapt = guessadapt:main']
    },

    install_requires=[
        'biopython'
    ],

    author='Michael Knudsen',
    author_email='michaelk@clin.au.dk',
    license='MIT'

)
