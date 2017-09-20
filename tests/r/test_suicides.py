from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.suicides import suicides


def test_suicides():
  """Test module suicides.py by downloading
   suicides.csv and testing shape of
   extracted data has 2 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = suicides(test_path)
  try:
    assert x_train.shape == (2, 2)
  except:
    shutil.rmtree(test_path)
    raise()
