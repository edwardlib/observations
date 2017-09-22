from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.yeast_d_mat import yeast_d_mat


def test_yeast_d_mat():
  """Test module yeast_d_mat.py by downloading
   yeast_d_mat.csv and testing shape of
   extracted data has 20 rows and 20 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = yeast_d_mat(test_path)
  try:
    assert x_train.shape == (20, 20)
  except:
    shutil.rmtree(test_path)
    raise()
