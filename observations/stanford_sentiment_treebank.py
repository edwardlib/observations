from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import os
import re

from observations.util import maybe_download_and_extract


def stanford_sentiment_treebank(path):
  """Load the Stanford Sentiment Treebank data set [@socher2013recursive].
  It consists of 8,544 training sentences, 2,210 test sentences, and
  1,101 validation sentences extracted from Rotten Tomatoes movie
  reviews. Each sentence is encoded as a parse tree with a sentiment
  label 0-4 (negative to positive) for each node.  Here we load the
  raw sentence and its overall sentiment label.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `trees/`.

  Returns:
    `(x_train, y_train), (x_test, y_test), (x_valid, y_valid)`,
    where each `x` is a list of strings (sentences) and each `y` is
    a NumPy array with the respective sentence-level sentiment label.
  """
  def _load(path):
    x = []
    y = []
    with open(path) as f:
      for line in f:
        sentence = ' '.join(re.sub("\(\d ", "", line).replace(
            ')', '').replace('-LRB-', '(').replace('-RRB-', ')').split())
        x.append(sentence)
        y.append(line[1])
    y = np.array(y, dtype=np.int)
    return x, y
  path = os.path.expanduser(path)
  directory = 'trees'
  if not os.path.exists(os.path.join(path, directory)):
    url = 'https://nlp.stanford.edu/sentiment/trainDevTestTrees_PTB.zip'
    maybe_download_and_extract(path, url)

  path = os.path.join(path, directory)
  x_train, y_train = _load(os.path.join(path, 'train.txt'))
  x_test, y_test = _load(os.path.join(path, 'test.txt'))
  x_valid, y_valid = _load(os.path.join(path, 'dev.txt'))
  return (x_train, y_train), (x_test, y_test), (x_valid, y_valid)
