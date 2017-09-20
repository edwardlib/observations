from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nidd_annual import nidd_annual


def test_nidd_annual():
  """Test module nidd_annual.py by downloading
   nidd_annual.csv and testing shape of
   extracted data has 35 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nidd_annual(test_path)
  try:
    assert x_train.shape == (35, 1)
  except:
    shutil.rmtree(test_path)
    raise()
