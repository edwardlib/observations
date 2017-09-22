from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.meap93 import meap93


def test_meap93():
  """Test module meap93.py by downloading
   meap93.csv and testing shape of
   extracted data has 408 rows and 17 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = meap93(test_path)
  try:
    assert x_train.shape == (408, 17)
  except:
    shutil.rmtree(test_path)
    raise()
