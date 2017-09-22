from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.volcano import volcano


def test_volcano():
  """Test module volcano.py by downloading
   volcano.csv and testing shape of
   extracted data has 87 rows and 61 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = volcano(test_path)
  try:
    assert x_train.shape == (87, 61)
  except:
    shutil.rmtree(test_path)
    raise()
