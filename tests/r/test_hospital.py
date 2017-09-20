from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hospital import hospital


def test_hospital():
  """Test module hospital.py by downloading
   hospital.csv and testing shape of
   extracted data has 3 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hospital(test_path)
  try:
    assert x_train.shape == (3, 3)
  except:
    shutil.rmtree(test_path)
    raise()
