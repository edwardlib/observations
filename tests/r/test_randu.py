from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.randu import randu


def test_randu():
  """Test module randu.py by downloading
   randu.csv and testing shape of
   extracted data has 400 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = randu(test_path)
  try:
    assert x_train.shape == (400, 3)
  except:
    shutil.rmtree(test_path)
    raise()
