from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.pension import pension


def test_pension():
  """Test module pension.py by downloading
   pension.csv and testing shape of
   extracted data has 194 rows and 19 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pension(test_path)
  try:
    assert x_train.shape == (194, 19)
  except:
    shutil.rmtree(test_path)
    raise()
