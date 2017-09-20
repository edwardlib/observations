from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cement import cement


def test_cement():
  """Test module cement.py by downloading
   cement.csv and testing shape of
   extracted data has 312 rows and 30 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cement(test_path)
  try:
    assert x_train.shape == (312, 30)
  except:
    shutil.rmtree(test_path)
    raise()
