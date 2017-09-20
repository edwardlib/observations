from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.wage1 import wage1


def test_wage1():
  """Test module wage1.py by downloading
   wage1.csv and testing shape of
   extracted data has 526 rows and 24 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wage1(test_path)
  try:
    assert x_train.shape == (526, 24)
  except:
    shutil.rmtree(test_path)
    raise()
