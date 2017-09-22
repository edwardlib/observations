from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.lowbrth import lowbrth


def test_lowbrth():
  """Test module lowbrth.py by downloading
   lowbrth.csv and testing shape of
   extracted data has 100 rows and 36 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = lowbrth(test_path)
  try:
    assert x_train.shape == (100, 36)
  except:
    shutil.rmtree(test_path)
    raise()
