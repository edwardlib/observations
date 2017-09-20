from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.npk import npk


def test_npk():
  """Test module npk.py by downloading
   npk.csv and testing shape of
   extracted data has 24 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = npk(test_path)
  try:
    assert x_train.shape == (24, 5)
  except:
    shutil.rmtree(test_path)
    raise()
