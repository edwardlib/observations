from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nbasal import nbasal


def test_nbasal():
  """Test module nbasal.py by downloading
   nbasal.csv and testing shape of
   extracted data has 269 rows and 22 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nbasal(test_path)
  try:
    assert x_train.shape == (269, 22)
  except:
    shutil.rmtree(test_path)
    raise()
