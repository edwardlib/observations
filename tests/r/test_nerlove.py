from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nerlove import nerlove


def test_nerlove():
  """Test module nerlove.py by downloading
   nerlove.csv and testing shape of
   extracted data has 159 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nerlove(test_path)
  try:
    assert x_train.shape == (159, 8)
  except:
    shutil.rmtree(test_path)
    raise()
