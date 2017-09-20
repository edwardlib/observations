from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.vocab import vocab


def test_vocab():
  """Test module vocab.py by downloading
   vocab.csv and testing shape of
   extracted data has 21638 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = vocab(test_path)
  try:
    assert x_train.shape == (21638, 4)
  except:
    shutil.rmtree(test_path)
    raise()
