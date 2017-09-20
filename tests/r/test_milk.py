from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.milk import milk


def test_milk():
  """Test module milk.py by downloading
   milk.csv and testing shape of
   extracted data has 86 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = milk(test_path)
  try:
    assert x_train.shape == (86, 8)
  except:
    shutil.rmtree(test_path)
    raise()
