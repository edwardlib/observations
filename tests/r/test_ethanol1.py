from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ethanol1 import ethanol1


def test_ethanol1():
  """Test module ethanol1.py by downloading
   ethanol1.csv and testing shape of
   extracted data has 16 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ethanol1(test_path)
  try:
    assert x_train.shape == (16, 3)
  except:
    shutil.rmtree(test_path)
    raise()
