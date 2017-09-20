from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mfblong import mfblong


def test_mfblong():
  """Test module mfblong.py by downloading
   mfblong.csv and testing shape of
   extracted data has 3000 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mfblong(test_path)
  try:
    assert x_train.shape == (3000, 10)
  except:
    shutil.rmtree(test_path)
    raise()
