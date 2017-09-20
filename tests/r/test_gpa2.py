from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.gpa2 import gpa2


def test_gpa2():
  """Test module gpa2.py by downloading
   gpa2.csv and testing shape of
   extracted data has 4137 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = gpa2(test_path)
  try:
    assert x_train.shape == (4137, 12)
  except:
    shutil.rmtree(test_path)
    raise()
