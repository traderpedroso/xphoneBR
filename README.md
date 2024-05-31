![Pypi Publish](https://github.com/traderpedroso/xphoneBR/actions/workflows/python-publish.yml/badge.svg)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/traderpedroso/xphoneBR)
[![License](https://img.shields.io/github/license/traderpedroso/xphoneBR)](https://github.com/traderpedroso/xphoneBR/blob/master/LICENSE)
[![PyPi downloads](https://img.shields.io/pypi/dm/xphonebr?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/xphonebr/)

# Python Phonemizer Brazilian portuguese 

`xphoneBR`  is a library for grapheme to phoneme conversion for Brazilian Portuguese based on Transformer models. 
It is intended to be used in text-to-speech production systems with high accuracy and efficiency.
You can choose between a forward Transformer model (trained with CTC) and its autoregressive
counterpart. The former is faster and more stable while the latter is slightly more accurate.

## Features

- [x] G2P
- [x] Normalization
- [ ] Bert Tokenizer


## Prerequisites

The library has been tested on Python 3.7 to 3.11.

## Installation

To install the latest version of `xphoneBR`, you can use pip:

```shell
pip install xphonebr -U
```
Or if you want to install from source, you can use:
```shell
pip install git+https://github.com/traderpedroso/xphoneBR.git
```



### Quickstart

#### for Transformer and faster and auto Normalization

```python
from xphonebr import Phonemizer


phones = Phonemizer(normalizer=True) 

phones.phonemise("Dra. Ana tem 45% da empresa & cia e iniciou as 8:45 de quinta feira do ano 2024 etc.  ")

output: 'dowˈtoɾə. ˈãnə ˈtẽ kwaˈɾẽtə ˈi ˈsĩkʊ ˈpox ˈsẽtʊ ˈda ẽˈpɾɛzə ˈi kõpãˈiə ˈi inisiˈow ˈas ˈoytʊ ˈɔɾəs ˈi kwaˈɾẽtə ˈi ˈsĩkʊ miˈnutʊs ˈdʒi ˈkĩtə ˈfeyɾə ˈdʊ ˈãnʊ ˈdoys ˈmiw ˈi ˈvĩtʃɪ ˈi ˈkwatɾʊ ˈit seˈteɾə.'

```
#### for autoregressive Transformer slightly more accurate and auto Normalization

```python
from xphonebr import Phonemizer


phones = Phonemizer(autoreg=True, normalizer=True) 

phones.phonemise("Dra. Ana tem 45% da empresa & cia e iniciou as 8:45 de quinta feira do ano 2024 etc.  ")

output: 'dowˈtoɾə. ˈãnə ˈtẽ kwaˈɾẽtə ˈi ˈsĩkʊ ˈpox ˈsẽtʊ ˈda ẽˈpɾɛzə ˈi kõpãˈiə ˈi inisiˈow ˈas ˈoytʊ ˈɔɾəs ˈi kwaˈɾẽtə ˈi ˈsĩkʊ miˈnutʊs ˈdʒi ˈkĩtə ˈfeyɾə ˈdʊ ˈãnʊ ˈdoys ˈmiw ˈi ˈvĩtʃɪ ˈi ˈkwatɾʊ ˈit seˈteɾə.'

```

#### for Normalization only

```python
from xphonebr import normalizer

normalizer("Dra. Ana tem 45% da empresa & cia e iniciou as 8:45 de quinta feira do ano 2024 etc.  ")

output: 'doutora. Ana tem quarenta e cinco por cento da empresa e companhia e iniciou as oito horas e quarenta e cinco minutos de quinta feira do ano dois mil e vinte e quatro et cetera.'

```

## Contributing

We welcome any contribution to `xphoneBR`. Here are some ways to contribute:

1. Report issues or suggest improvements by opening an [issue](https://github.com/traderpedroso/xphoneBR/issues).
2. Contribute with code to fix issues or add features via a [Pull Request](https://github.com/traderpedroso/xphoneBR/pulls).

Before submitting a pull request, please make sure your codes are well formatted and tested.

## Acknowledgements

I would like to express my gratitude to [@as-ideas](https://github.com/as-ideas) for creating the initial project. Their work has been an invaluable starting point for my modifications and improvements for Brazilian portuguese.
