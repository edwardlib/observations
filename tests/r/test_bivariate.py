from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bivariate import bivariate


def test_bivariate():
  """Test module bivariate.py by downloading
   bivariate.csv and testing shape of
   extracted data has 78 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bivariate(test_path)
  try:
    assert x_train.shape == (78, 6)
  except:
    shutil.rmtree(test_path)
    raise()
