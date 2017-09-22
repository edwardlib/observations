from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.pyx import pyx


def test_pyx():
  """Test module pyx.py by downloading
   pyx.csv and testing shape of
   extracted data has 72 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pyx(test_path)
  try:
    assert x_train.shape == (72, 4)
  except:
    shutil.rmtree(test_path)
    raise()
