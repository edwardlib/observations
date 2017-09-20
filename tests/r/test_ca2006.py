from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ca2006 import ca2006


def test_ca2006():
  """Test module ca2006.py by downloading
   ca2006.csv and testing shape of
   extracted data has 53 rows and 13 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ca2006(test_path)
  try:
    assert x_train.shape == (53, 13)
  except:
    shutil.rmtree(test_path)
    raise()
