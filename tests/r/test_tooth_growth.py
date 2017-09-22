from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.tooth_growth import tooth_growth


def test_tooth_growth():
  """Test module tooth_growth.py by downloading
   tooth_growth.csv and testing shape of
   extracted data has 60 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = tooth_growth(test_path)
  try:
    assert x_train.shape == (60, 3)
  except:
    shutil.rmtree(test_path)
    raise()
