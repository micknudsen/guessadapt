[![install with conda](https://anaconda.org/micknudsen/guessadapt/badges/version.svg)](https://anaconda.org/micknudsen/guessadapt) ![CI](https://github.com/micknudsen/guessadapt/workflows/CI/badge.svg?branch=master) [![Coverage Status](https://coveralls.io/repos/github/micknudsen/guessadapt/badge.svg?branch=master)](https://coveralls.io/github/micknudsen/guessadapt?branch=master)





# guessadapt

Given a FASTQ file and a list of adapter sequences, `guessadapt` simply counts the number of occurences of each adapter and returns sorted list of counts. That's it!


```
$ guessadapt --help
usage: guessadapt [-h] [--limit LIMIT] [--adapters ADAPTERS] fastq

positional arguments:
  fastq                 path to input FASTQ file

optional arguments:
  -h, --help            show this help message and exit
  --limit LIMIT, -n LIMIT
                        maximal number of reads to consider
  --adapters ADAPTERS, -a ADAPTERS
                        commma-separated list of adapters (default:
                        AGATCGGAAGAGC,TGGAATTCTCGG,CTGTCTCTTATA)
```

The simplest way to install `guessadapt` is by using conda:

```
$ conda install -c micknudsen guessadapt
```
