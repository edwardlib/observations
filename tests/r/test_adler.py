from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.adler import adler


def test_adler():
  """Test module adler.py by downloading
   adler.csv and testing shape of
   extracted data has 97 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = adler(test_path)
  try:
    assert x_train.shape == (97, 3)
  except:
    shutil.rmtree(test_path)
    raise()
