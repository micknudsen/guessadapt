from setuptools import setup, find_packages

setup(

    name='guessadapt',

    packages=find_packages('src'),
    package_dir={'': 'src'},

    entry_points={
        'console_scripts': ['guessadapt = guessadapt.client:main']
    },

    python_requires='>=3.6',

    install_requires=[
        'biopython'
    ],

    author='Michael Knudsen',
    author_email='micknudsen@gmail.com',
    license='MIT'

)
