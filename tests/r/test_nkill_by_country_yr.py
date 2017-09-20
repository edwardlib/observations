from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nkill_by_country_yr import nkill_by_country_yr


def test_nkill_by_country_yr():
  """Test module nkill_by_country_yr.py by downloading
   nkill_by_country_yr.csv and testing shape of
   extracted data has 206 rows and 45 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nkill_by_country_yr(test_path)
  try:
    assert x_train.shape == (206, 45)
  except:
    shutil.rmtree(test_path)
    raise()
