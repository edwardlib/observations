from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sunspot_month import sunspot_month


def test_sunspot_month():
  """Test module sunspot_month.py by downloading
   sunspot_month.csv and testing shape of
   extracted data has 3177 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sunspot_month(test_path)
  try:
    assert x_train.shape == (3177, 2)
  except:
    shutil.rmtree(test_path)
    raise()
