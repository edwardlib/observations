from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os

from observations.util import maybe_download_and_extract


def sick(path):
  """Load the Sentences Involving Compositional Knowledge (SICK) data
  set [@marelli2014sick]. It consists of ~10,000 English sentence
  pairs, where each pair is annotated for relatedness and entailment.
  There are 923 pairs within the [1,2) range, 1373 pairs within the
  [2,3) range, 3872 pairs within the [3,4) range, and 3672 pairs
  within the [4,5] range; the entailment annotation led to 5595
  neutral pairs, 1424 contradiction pairs, and 2821 entailment pairs.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filenames are
      `SICK_train.txt`, `SICK_test_annotated.txt`, `SICK_trial.txt`.

  Returns:
    Tuple of dict `x_train, x_test, x_valid`. Each dict has keys
    'relatedness_score', 'pair_ID', 'sentence_A', 'sentence_B',
    'entailment_judgment'. The kth value in each key comprises of the
    kth sentence pair and its annotations.
  """
  def _load(path):
    with open(path) as f:
      iterator = csv.reader(f, delimiter='\t')
      keys = next(iterator)
      values = [[value] for value in next(iterator)]
      for row in iterator:
        for j in range(len(keys)):
          values[j].append(row[j])
    data = {k: v for k, v in zip(keys, values)}
    data['pair_ID'] = np.array(data['pair_ID'], dtype=np.int)
    data['relatedness_score'] = np.array(
        data['relatedness_score'], dtype=np.float)
    return data
  path = os.path.expanduser(path)
  url = 'http://alt.qcri.org/semeval2014/task1/data/uploads/'
  train_filename = 'SICK_train.txt'
  test_filename = 'SICK_test_annotated.txt'
  valid_filename = 'SICK_trial.txt'
  if not os.path.exists(os.path.join(path, train_filename)):
    maybe_download_and_extract(path, url + 'sick_train.zip')
  if not os.path.exists(os.path.join(path, test_filename)):
    maybe_download_and_extract(path, url + 'sick_test_annotated.zip')
  if not os.path.exists(os.path.join(path, valid_filename)):
    maybe_download_and_extract(path, url + 'sick_trial.zip')

  x_train = _load(os.path.join(path, train_filename))
  x_test = _load(os.path.join(path, test_filename))
  x_valid = _load(os.path.join(path, valid_filename))
  return x_train, x_test, x_valid
