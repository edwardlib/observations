from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.males1 import males1


def test_males1():
  """Test module males1.py by downloading
   males1.csv and testing shape of
   extracted data has 4360 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = males1(test_path)
  try:
    assert x_train.shape == (4360, 12)
  except:
    shutil.rmtree(test_path)
    raise()
