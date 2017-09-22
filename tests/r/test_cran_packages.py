from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cran_packages import cran_packages


def test_cran_packages():
  """Test module cran_packages.py by downloading
   cran_packages.csv and testing shape of
   extracted data has 29 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cran_packages(test_path)
  try:
    assert x_train.shape == (29, 4)
  except:
    shutil.rmtree(test_path)
    raise()
