from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.myeloid import myeloid


def test_myeloid():
  """Test module myeloid.py by downloading
   myeloid.csv and testing shape of
   extracted data has 646 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = myeloid(test_path)
  try:
    assert x_train.shape == (646, 7)
  except:
    shutil.rmtree(test_path)
    raise()
