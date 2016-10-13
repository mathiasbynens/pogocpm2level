# pogocpm2level [![Build status](https://travis-ci.org/mathiasbynens/pogocpm2level.svg?branch=master)](https://travis-ci.org/mathiasbynens/pogocpm2level) [![PyPI version](https://img.shields.io/pypi/v/pogocpm2level.svg)](https://pypi.python.org/pypi/pogocpm2level)

_pogocpm2level_ makes it easy to calculate the level of a Pokémon in Pokémon GO based on its total CP multiplier value (i.e. the sum of its `cp_multiplier` and its `additional_cp_multiplier`, if any).

## Installation

Using [pip](https://pip.pypa.io/):

```sh
$ pip install pogocpm2level
```

## Usage

```py
from pogocpm2level import cpm2level

level = cpm2level(0.491)
print level
# → 13.5
```

## Author

| [![twitter/mathias](https://gravatar.com/avatar/24e08a9ea84deb17ae121074d0f17125?s=70)](https://twitter.com/mathias "Follow @mathias on Twitter") |
|---|
| [Mathias Bynens](https://mathiasbynens.be/) |

## License

_pogocpm2level_ is available under the [MIT](https://mths.be/mit) license.
