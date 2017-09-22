from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.logan import logan


def test_logan():
  """Test module logan.py by downloading
   logan.csv and testing shape of
   extracted data has 838 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = logan(test_path)
  try:
    assert x_train.shape == (838, 4)
  except:
    shutil.rmtree(test_path)
    raise()
