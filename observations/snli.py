from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import numpy as np
import os

from observations.util import maybe_download_and_extract


def snli(path):
  """Load the Stanford Natural Language Inference (SNLI) corpus
  [@bowman2015large]. It is a collection of 570,000 human-written
  English sentence pairs manually labeled for balanced classification
  with the labels entailment, contradiction, and neutral.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `snli_1.0/`.

  Returns:
    Tuple of dict `x_train, x_test, x_valid`. Each dict has keys
    'sentence1', 'sentence2', 'label'. The kth value in each key,
    e.g., `x_train['sentence1'][k], x_train['sentence2'][k],
    x_train['label'][k]` comprises of a sentence pair and its label.
  """
  def _yield_examples(fn):
    for line in open(fn):
      data = json.loads(line)
      label = data['gold_label']
      s1 = ' '.join(data['sentence1_binary_parse'].replace(
          '(', ' ').replace(')', ' ').replace('-LRB-', '(').replace(
          '-RRB-', ')').split())
      s2 = ' '.join(data['sentence2_binary_parse'].replace(
          '(', ' ').replace(')', ' ').replace('-LRB-', '(').replace(
          '-RRB-', ')').split())
      if label == '-':
        continue
      yield (label, s1, s2)
  def _load(path):
    raw_data = list(_yield_examples(path))
    sentence1 = [s1 for _, s1, _ in raw_data]
    sentence2 = [s2 for _, _, s2 in raw_data]
    labels = {'contradiction': 0, 'neutral': 1, 'entailment': 2}
    label = np.array([labels[l] for l, _, _ in raw_data])
    return {'sentence1': sentence1, 'sentence2': sentence2, 'label': label}
  path = os.path.expanduser(path)
  directory = 'snli_1.0'
  if not os.path.exists(os.path.join(path, directory)):
    url = 'https://nlp.stanford.edu/projects/snli/snli_1.0.zip'
    maybe_download_and_extract(path, url)

  path = os.path.join(path, directory)
  x_train = _load(os.path.join(path, 'snli_1.0_train.jsonl'))
  x_test = _load(os.path.join(path, 'snli_1.0_test.jsonl'))
  x_valid = _load(os.path.join(path, 'snli_1.0_dev.jsonl'))
  return x_train, x_test, x_valid
