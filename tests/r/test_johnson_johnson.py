from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.johnson_johnson import johnson_johnson


def test_johnson_johnson():
  """Test module johnson_johnson.py by downloading
   johnson_johnson.csv and testing shape of
   extracted data has 84 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = johnson_johnson(test_path)
  try:
    assert x_train.shape == (84, 2)
  except:
    shutil.rmtree(test_path)
    raise()
