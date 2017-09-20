from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.intqrt import intqrt


def test_intqrt():
  """Test module intqrt.py by downloading
   intqrt.csv and testing shape of
   extracted data has 124 rows and 23 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = intqrt(test_path)
  try:
    assert x_train.shape == (124, 23)
  except:
    shutil.rmtree(test_path)
    raise()
