from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.transplant import transplant


def test_transplant():
  """Test module transplant.py by downloading
   transplant.csv and testing shape of
   extracted data has 815 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = transplant(test_path)
  try:
    assert x_train.shape == (815, 6)
  except:
    shutil.rmtree(test_path)
    raise()
