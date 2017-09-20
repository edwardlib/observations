from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.wages import wages


def test_wages():
  """Test module wages.py by downloading
   wages.csv and testing shape of
   extracted data has 4165 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wages(test_path)
  try:
    assert x_train.shape == (4165, 12)
  except:
    shutil.rmtree(test_path)
    raise()
