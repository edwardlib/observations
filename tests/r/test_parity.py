from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.parity import parity


def test_parity():
  """Test module parity.py by downloading
   parity.csv and testing shape of
   extracted data has 1768 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = parity(test_path)
  try:
    assert x_train.shape == (1768, 9)
  except:
    shutil.rmtree(test_path)
    raise()
