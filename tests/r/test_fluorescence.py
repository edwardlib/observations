from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fluorescence import fluorescence


def test_fluorescence():
  """Test module fluorescence.py by downloading
   fluorescence.csv and testing shape of
   extracted data has 51 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fluorescence(test_path)
  try:
    assert x_train.shape == (51, 2)
  except:
    shutil.rmtree(test_path)
    raise()
