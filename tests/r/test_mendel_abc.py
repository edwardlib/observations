from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mendel_abc import mendel_abc


def test_mendel_abc():
  """Test module mendel_abc.py by downloading
   mendel_abc.csv and testing shape of
   extracted data has 27 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mendel_abc(test_path)
  try:
    assert x_train.shape == (27, 4)
  except:
    shutil.rmtree(test_path)
    raise()
