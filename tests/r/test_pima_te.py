from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.pima_te import pima_te


def test_pima_te():
  """Test module pima_te.py by downloading
   pima_te.csv and testing shape of
   extracted data has 332 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pima_te(test_path)
  try:
    assert x_train.shape == (332, 8)
  except:
    shutil.rmtree(test_path)
    raise()
