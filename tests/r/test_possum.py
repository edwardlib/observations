from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.possum import possum


def test_possum():
  """Test module possum.py by downloading
   possum.csv and testing shape of
   extracted data has 104 rows and 14 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = possum(test_path)
  try:
    assert x_train.shape == (104, 14)
  except:
    shutil.rmtree(test_path)
    raise()
