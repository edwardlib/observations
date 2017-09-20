from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.us_gdp_presidents import us_gdp_presidents


def test_us_gdp_presidents():
  """Test module us_gdp_presidents.py by downloading
   us_gdp_presidents.csv and testing shape of
   extracted data has 259 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = us_gdp_presidents(test_path)
  try:
    assert x_train.shape == (259, 12)
  except:
    shutil.rmtree(test_path)
    raise()
