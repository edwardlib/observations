from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sum_hes import sum_hes


def test_sum_hes():
  """Test module sum_hes.py by downloading
   sum_hes.csv and testing shape of
   extracted data has 3250 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sum_hes(test_path)
  try:
    assert x_train.shape == (3250, 7)
  except:
    shutil.rmtree(test_path)
    raise()
