from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.archery_data import archery_data


def test_archery_data():
  """Test module archery_data.py by downloading
   archery_data.csv and testing shape of
   extracted data has 18 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = archery_data(test_path)
  try:
    assert x_train.shape == (18, 7)
  except:
    shutil.rmtree(test_path)
    raise()
