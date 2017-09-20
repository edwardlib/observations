from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fair1 import fair1


def test_fair1():
  """Test module fair1.py by downloading
   fair1.csv and testing shape of
   extracted data has 21 rows and 28 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fair1(test_path)
  try:
    assert x_train.shape == (21, 28)
  except:
    shutil.rmtree(test_path)
    raise()
