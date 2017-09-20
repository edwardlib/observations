from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.porsche_price import porsche_price


def test_porsche_price():
  """Test module porsche_price.py by downloading
   porsche_price.csv and testing shape of
   extracted data has 30 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = porsche_price(test_path)
  try:
    assert x_train.shape == (30, 3)
  except:
    shutil.rmtree(test_path)
    raise()
