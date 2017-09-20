from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.gpa3 import gpa3


def test_gpa3():
  """Test module gpa3.py by downloading
   gpa3.csv and testing shape of
   extracted data has 732 rows and 23 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = gpa3(test_path)
  try:
    assert x_train.shape == (732, 23)
  except:
    shutil.rmtree(test_path)
    raise()
