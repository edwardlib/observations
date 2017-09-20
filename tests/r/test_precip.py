from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.precip import precip


def test_precip():
  """Test module precip.py by downloading
   precip.csv and testing shape of
   extracted data has 70 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = precip(test_path)
  try:
    assert x_train.shape == (70, 1)
  except:
    shutil.rmtree(test_path)
    raise()
