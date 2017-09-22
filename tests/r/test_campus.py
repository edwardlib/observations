from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.campus import campus


def test_campus():
  """Test module campus.py by downloading
   campus.csv and testing shape of
   extracted data has 97 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = campus(test_path)
  try:
    assert x_train.shape == (97, 7)
  except:
    shutil.rmtree(test_path)
    raise()
