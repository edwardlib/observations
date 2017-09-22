from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.acf1 import acf1


def test_acf1():
  """Test module acf1.py by downloading
   acf1.csv and testing shape of
   extracted data has 22 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = acf1(test_path)
  try:
    assert x_train.shape == (22, 2)
  except:
    shutil.rmtree(test_path)
    raise()
