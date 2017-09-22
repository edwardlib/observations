from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.birthwt import birthwt


def test_birthwt():
  """Test module birthwt.py by downloading
   birthwt.csv and testing shape of
   extracted data has 189 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = birthwt(test_path)
  try:
    assert x_train.shape == (189, 10)
  except:
    shutil.rmtree(test_path)
    raise()
