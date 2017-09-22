from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.science import science


def test_science():
  """Test module science.py by downloading
   science.csv and testing shape of
   extracted data has 1385 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = science(test_path)
  try:
    assert x_train.shape == (1385, 7)
  except:
    shutil.rmtree(test_path)
    raise()
