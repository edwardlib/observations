from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.airquality import airquality


def test_airquality():
  """Test module airquality.py by downloading
   airquality.csv and testing shape of
   extracted data has 153 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = airquality(test_path)
  try:
    assert x_train.shape == (153, 6)
  except:
    shutil.rmtree(test_path)
    raise()
