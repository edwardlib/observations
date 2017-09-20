from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.pines import pines


def test_pines():
  """Test module pines.py by downloading
   pines.csv and testing shape of
   extracted data has 1000 rows and 15 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pines(test_path)
  try:
    assert x_train.shape == (1000, 15)
  except:
    shutil.rmtree(test_path)
    raise()
