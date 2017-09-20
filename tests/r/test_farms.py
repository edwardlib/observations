from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.farms import farms


def test_farms():
  """Test module farms.py by downloading
   farms.csv and testing shape of
   extracted data has 20 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = farms(test_path)
  try:
    assert x_train.shape == (20, 4)
  except:
    shutil.rmtree(test_path)
    raise()
