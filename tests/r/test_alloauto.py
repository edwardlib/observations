from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.alloauto import alloauto


def test_alloauto():
  """Test module alloauto.py by downloading
   alloauto.csv and testing shape of
   extracted data has 101 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = alloauto(test_path)
  try:
    assert x_train.shape == (101, 3)
  except:
    shutil.rmtree(test_path)
    raise()
