from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.kakadu import kakadu


def test_kakadu():
  """Test module kakadu.py by downloading
   kakadu.csv and testing shape of
   extracted data has 1827 rows and 22 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = kakadu(test_path)
  try:
    assert x_train.shape == (1827, 22)
  except:
    shutil.rmtree(test_path)
    raise()
