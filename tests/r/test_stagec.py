from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.stagec import stagec


def test_stagec():
  """Test module stagec.py by downloading
   stagec.csv and testing shape of
   extracted data has 146 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = stagec(test_path)
  try:
    assert x_train.shape == (146, 8)
  except:
    shutil.rmtree(test_path)
    raise()
