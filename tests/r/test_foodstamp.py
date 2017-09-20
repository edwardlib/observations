from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.foodstamp import foodstamp


def test_foodstamp():
  """Test module foodstamp.py by downloading
   foodstamp.csv and testing shape of
   extracted data has 150 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = foodstamp(test_path)
  try:
    assert x_train.shape == (150, 4)
  except:
    shutil.rmtree(test_path)
    raise()
