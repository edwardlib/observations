from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.us_crime import us_crime


def test_us_crime():
  """Test module us_crime.py by downloading
   us_crime.csv and testing shape of
   extracted data has 47 rows and 16 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = us_crime(test_path)
  try:
    assert x_train.shape == (47, 16)
  except:
    shutil.rmtree(test_path)
    raise()
