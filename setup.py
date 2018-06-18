from setuptools import setup, find_packages

setup(

    name='guessadapt',

    packages=find_packages('src'),
    package_dir={'': 'src'},

    author='Michael Knudsen',
    author_email='michaelk@clin.au.dk',
    license='MIT'

)