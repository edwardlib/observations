from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.caravan import caravan


def test_caravan():
  """Test module caravan.py by downloading
   caravan.csv and testing shape of
   extracted data has 5822 rows and 86 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = caravan(test_path)
  try:
    assert x_train.shape == (5822, 86)
  except:
    shutil.rmtree(test_path)
    raise()
