from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sna_ex import sna_ex


def test_sna_ex():
  """Test module sna_ex.py by downloading
   sna_ex.csv and testing shape of
   extracted data has 0 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sna_ex(test_path)
  try:
    assert x_train.shape == (0, 5)
  except:
    shutil.rmtree(test_path)
    raise()
