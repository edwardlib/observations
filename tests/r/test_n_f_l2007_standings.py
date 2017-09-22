from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.n_f_l2007_standings import n_f_l2007_standings


def test_n_f_l2007_standings():
  """Test module n_f_l2007_standings.py by downloading
   n_f_l2007_standings.csv and testing shape of
   extracted data has 32 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = n_f_l2007_standings(test_path)
  try:
    assert x_train.shape == (32, 10)
  except:
    shutil.rmtree(test_path)
    raise()
