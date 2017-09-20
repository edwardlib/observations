from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.women import women


def test_women():
  """Test module women.py by downloading
   women.csv and testing shape of
   extracted data has 15 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = women(test_path)
  try:
    assert x_train.shape == (15, 2)
  except:
    shutil.rmtree(test_path)
    raise()
