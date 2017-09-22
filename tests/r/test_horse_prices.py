from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.horse_prices import horse_prices


def test_horse_prices():
  """Test module horse_prices.py by downloading
   horse_prices.csv and testing shape of
   extracted data has 50 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = horse_prices(test_path)
  try:
    assert x_train.shape == (50, 5)
  except:
    shutil.rmtree(test_path)
    raise()
