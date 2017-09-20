from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nidd_thresh import nidd_thresh


def test_nidd_thresh():
  """Test module nidd_thresh.py by downloading
   nidd_thresh.csv and testing shape of
   extracted data has 154 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nidd_thresh(test_path)
  try:
    assert x_train.shape == (154, 1)
  except:
    shutil.rmtree(test_path)
    raise()
