from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.catsup import catsup


def test_catsup():
  """Test module catsup.py by downloading
   catsup.csv and testing shape of
   extracted data has 2798 rows and 14 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = catsup(test_path)
  try:
    assert x_train.shape == (2798, 14)
  except:
    shutil.rmtree(test_path)
    raise()
