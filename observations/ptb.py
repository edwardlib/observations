from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import os

from observations.util import maybe_download_and_extract


def ptb(path):
  """Load the Penn Treebank data set (Marcus et al., 1993). The
  dataset is preprocessed and has a vocabulary of 10,000 words,
  including the end-of-sentence marker and a special symbol (<unk>)
  for rare words. There are 929,589 training words, 73,760 validation
  words, and 82,430 test words.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `simple-examples/`.

  Returns:
    Tuple of str `x_train, x_test, x_valid`.
  """
  path = os.path.expanduser(path)
  if not os.path.exists(os.path.join(path, 'simple-examples')):
    url = 'http://www.fit.vutbr.cz/~imikolov/rnnlm/simple-examples.tgz'
    maybe_download_and_extract(path, url)

  path = os.path.join(path, 'simple-examples/data')
  with open(os.path.join(path, 'ptb.train.txt')) as f:
    x_train = f.read().decode("utf-8").replace("\n", "<eos>")
  with open(os.path.join(path, 'ptb.test.txt')) as f:
    x_test = f.read().decode("utf-8").replace("\n", "<eos>")
  with open(os.path.join(path, 'ptb.valid.txt')) as f:
    x_valid = f.read().decode("utf-8").replace("\n", "<eos>")
  return x_train, x_test, x_valid
