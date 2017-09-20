from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bwght import bwght


def test_bwght():
  """Test module bwght.py by downloading
   bwght.csv and testing shape of
   extracted data has 1388 rows and 14 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bwght(test_path)
  try:
    assert x_train.shape == (1388, 14)
  except:
    shutil.rmtree(test_path)
    raise()
