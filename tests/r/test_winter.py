from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.winter import winter


def test_winter():
  """Test module winter.py by downloading
   winter.csv and testing shape of
   extracted data has 532 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = winter(test_path)
  try:
    assert x_train.shape == (532, 5)
  except:
    shutil.rmtree(test_path)
    raise()
