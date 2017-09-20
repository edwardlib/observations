from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.leukemia import leukemia


def test_leukemia():
  """Test module leukemia.py by downloading
   leukemia.csv and testing shape of
   extracted data has 23 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = leukemia(test_path)
  try:
    assert x_train.shape == (23, 3)
  except:
    shutil.rmtree(test_path)
    raise()
