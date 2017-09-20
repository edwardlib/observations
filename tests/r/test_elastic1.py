from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.elastic1 import elastic1


def test_elastic1():
  """Test module elastic1.py by downloading
   elastic1.csv and testing shape of
   extracted data has 7 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = elastic1(test_path)
  try:
    assert x_train.shape == (7, 2)
  except:
    shutil.rmtree(test_path)
    raise()
