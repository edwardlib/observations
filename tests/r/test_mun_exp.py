from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mun_exp import mun_exp


def test_mun_exp():
  """Test module mun_exp.py by downloading
   mun_exp.csv and testing shape of
   extracted data has 2385 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mun_exp(test_path)
  try:
    assert x_train.shape == (2385, 5)
  except:
    shutil.rmtree(test_path)
    raise()
