from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.n_cbirths import n_cbirths


def test_n_cbirths():
  """Test module n_cbirths.py by downloading
   n_cbirths.csv and testing shape of
   extracted data has 1450 rows and 15 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = n_cbirths(test_path)
  try:
    assert x_train.shape == (1450, 15)
  except:
    shutil.rmtree(test_path)
    raise()
