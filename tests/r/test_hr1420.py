from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hr1420 import hr1420


def test_hr1420():
  """Test module hr1420.py by downloading
   hr1420.csv and testing shape of
   extracted data has 147849 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hr1420(test_path)
  try:
    assert x_train.shape == (147849, 5)
  except:
    shutil.rmtree(test_path)
    raise()
