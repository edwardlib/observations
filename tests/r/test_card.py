from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.card import card


def test_card():
  """Test module card.py by downloading
   card.csv and testing shape of
   extracted data has 3010 rows and 34 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = card(test_path)
  try:
    assert x_train.shape == (3010, 34)
  except:
    shutil.rmtree(test_path)
    raise()
