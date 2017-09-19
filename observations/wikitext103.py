from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import io
import os

from observations.util import maybe_download_and_extract


def wikitext103(path, raw=False):
  """Load the Wikitext-103 data set [@merity2016pointer].
  The dataset consists of Wikipedia articles fitting the Good or
  Featured article criteria and has a vocabulary of 267,735 words.
  There are 103,227,021 training, 217,646 validation, and 245,569 test
  tokens.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `wikitext-2/`.
    raw: bool, optional.
      Whether to load the raw data, which does not preprocess any
      tokens into <unk> and newlines into <eos>.

  Returns:
    Tuple of str `x_train, x_valid, x_test`.
  """
  path = os.path.expanduser(path)
  if raw:
    url = 'https://s3.amazonaws.com/research.metamind.io/wikitext/' \
          'wikitext-103-raw-v1.zip'
    directory = 'wikitext-103-raw'
    extension = '.raw'
  else:
    url = 'https://s3.amazonaws.com/research.metamind.io/wikitext/' \
          'wikitext-103-v1.zip'
    directory = 'wikitext-103'
    extension = '.tokens'
  if not os.path.exists(os.path.join(path, directory)):
    maybe_download_and_extract(path, url)

  path = os.path.join(path, directory)
  with io.open(os.path.join(path, 'wiki.train' + extension),
               encoding='utf-8') as f:
    x_train = f.read()
  with io.open(os.path.join(path, 'wiki.test' + extension),
               encoding='utf-8') as f:
    x_test = f.read()
  with io.open(os.path.join(path, 'wiki.valid' + extension),
               encoding='utf-8') as f:
    x_valid = f.read()
  if not raw:
    x_train = x_train.replace("\n", "<eos>")
    x_test = x_test.replace("\n", "<eos>")
    x_valid = x_valid.replace("\n", "<eos>")
  return x_train, x_test, x_valid
