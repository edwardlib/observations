from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.arabidopsis import arabidopsis


def test_arabidopsis():
  """Test module arabidopsis.py by downloading
   arabidopsis.csv and testing shape of
   extracted data has 625 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = arabidopsis(test_path)
  try:
    assert x_train.shape == (625, 8)
  except:
    shutil.rmtree(test_path)
    raise()
