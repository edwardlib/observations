from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.religion_gdp import religion_gdp


def test_religion_gdp():
  """Test module religion_gdp.py by downloading
   religion_gdp.csv and testing shape of
   extracted data has 44 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = religion_gdp(test_path)
  try:
    assert x_train.shape == (44, 9)
  except:
    shutil.rmtree(test_path)
    raise()
