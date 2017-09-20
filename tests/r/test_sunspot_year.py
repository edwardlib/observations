from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sunspot_year import sunspot_year


def test_sunspot_year():
  """Test module sunspot_year.py by downloading
   sunspot_year.csv and testing shape of
   extracted data has 289 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sunspot_year(test_path)
  try:
    assert x_train.shape == (289, 2)
  except:
    shutil.rmtree(test_path)
    raise()
