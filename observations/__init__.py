"""[Observations](https://github.com/edwardlib/observations) provides
a one line Python API for loading standard data sets in machine
learning. It automates the process from downloading, extracting,
loading, and preprocessing data. Observations helps keep the workflow
reproducible and follow sensible standards.

Observations is a standalone Python library and must be installed
separate from Edward.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from observations.abalone import abalone
from observations.boston_housing import boston_housing
from observations.caltech101_silhouettes import caltech101_silhouettes
from observations.celeba import celeba
from observations.celegans import celegans
from observations.cifar10 import cifar10
from observations.cifar100 import cifar100
from observations.crabs import crabs
from observations.enwik8 import enwik8
from observations.fashion_mnist import fashion_mnist
from observations.insteval import insteval
from observations.iris import iris
from observations.jsb_chorales import jsb_chorales
from observations.karate import karate
from observations.lsun import lsun
from observations.mnist import mnist
from observations.multi_mnist import multi_mnist
from observations.nips import nips
from observations.ptb import ptb
from observations.sick import sick
from observations.small32_imagenet import small32_imagenet
from observations.small64_imagenet import small64_imagenet
from observations.snli import snli
from observations.stanford_sentiment_treebank import stanford_sentiment_treebank
from observations.svhn import svhn
from observations.text8 import text8
from observations.util import maybe_download_and_extract
from observations.version import __version__, VERSION
from observations.wikitext2 import wikitext2
from observations.wikitext103 import wikitext103
from observations.wine import wine
from observations.yelp17 import yelp17


def remove_undocumented(module_name, allowed_exception_list=None):
  """Removes symbols in a module that are not referenced by a docstring.

  Args:
    module_name: the name of the module (usually `__name__`).
    allowed_exception_list: a list of names that should not be removed.

  Returns:
    None
  """
  import sys as _sys
  current_symbols = set(dir(_sys.modules[module_name]))
  should_have = allowed_exception_list or []
  extra_symbols = current_symbols - set(should_have)
  target_module = _sys.modules[module_name]
  for extra_symbol in extra_symbols:
    # Skip over __file__, etc. Also preserves internal symbols.
    if extra_symbol.startswith('_'):
      continue
    fully_qualified_name = module_name + '.' + extra_symbol
    delattr(target_module, extra_symbol)


# Export modules and constants.
_allowed_symbols = [
    'abalone',
    'boston_housing',
    'caltech101_silhouettes',
    'celeba',
    'celegans',
    'cifar10',
    'cifar100',
    'crabs',
    'enwik8',
    'fashion_mnist',
    'insteval',
    'iris',
    'jsb_chorales',
    'karate',
    'lsun',
    'mnist',
    'multi_mnist',
    'nips',
    'ptb',
    'sick',
    'small32_imagenet',
    'small64_imagenet',
    'snli',
    'stanford_sentiment_treebank',
    'svhn',
    'text8',
    'maybe_download_and_extract',
    'wikitext2',
    'wikitext103',
    'wine',
    'yelp17',
    '__version__',
    'VERSION',
]

# Remove all extra symbols that don't have a docstring or are not explicitly
# referenced in the whitelist.
remove_undocumented(__name__, _allowed_symbols)
