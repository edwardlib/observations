from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sitka import sitka


def test_sitka():
  """Test module sitka.py by downloading
   sitka.csv and testing shape of
   extracted data has 395 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sitka(test_path)
  try:
    assert x_train.shape == (395, 4)
  except:
    shutil.rmtree(test_path)
    raise()
