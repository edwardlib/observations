from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.amis import amis


def test_amis():
  """Test module amis.py by downloading
   amis.csv and testing shape of
   extracted data has 8437 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = amis(test_path)
  try:
    assert x_train.shape == (8437, 4)
  except:
    shutil.rmtree(test_path)
    raise()
