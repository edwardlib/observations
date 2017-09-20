from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cigarette import cigarette


def test_cigarette():
  """Test module cigarette.py by downloading
   cigarette.csv and testing shape of
   extracted data has 528 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cigarette(test_path)
  try:
    assert x_train.shape == (528, 9)
  except:
    shutil.rmtree(test_path)
    raise()
