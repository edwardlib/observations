from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.gdp_infant_mortality import gdp_infant_mortality


def test_gdp_infant_mortality():
  """Test module gdp_infant_mortality.py by downloading
   gdp_infant_mortality.csv and testing shape of
   extracted data has 207 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = gdp_infant_mortality(test_path)
  try:
    assert x_train.shape == (207, 2)
  except:
    shutil.rmtree(test_path)
    raise()
