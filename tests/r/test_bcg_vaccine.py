from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bcg_vaccine import bcg_vaccine


def test_bcg_vaccine():
  """Test module bcg_vaccine.py by downloading
   bcg_vaccine.csv and testing shape of
   extracted data has 13 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bcg_vaccine(test_path)
  try:
    assert x_train.shape == (13, 7)
  except:
    shutil.rmtree(test_path)
    raise()
