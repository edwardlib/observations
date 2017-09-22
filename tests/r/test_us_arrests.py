from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.us_arrests import us_arrests


def test_us_arrests():
  """Test module us_arrests.py by downloading
   us_arrests.csv and testing shape of
   extracted data has 50 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = us_arrests(test_path)
  try:
    assert x_train.shape == (50, 4)
  except:
    shutil.rmtree(test_path)
    raise()
