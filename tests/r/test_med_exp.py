from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.med_exp import med_exp


def test_med_exp():
  """Test module med_exp.py by downloading
   med_exp.csv and testing shape of
   extracted data has 5574 rows and 15 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = med_exp(test_path)
  try:
    assert x_train.shape == (5574, 15)
  except:
    shutil.rmtree(test_path)
    raise()
