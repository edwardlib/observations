from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.crohn_d import crohn_d


def test_crohn_d():
  """Test module crohn_d.py by downloading
   crohn_d.csv and testing shape of
   extracted data has 117 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = crohn_d(test_path)
  try:
    assert x_train.shape == (117, 9)
  except:
    shutil.rmtree(test_path)
    raise()
