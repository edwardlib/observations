from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.womensrole import womensrole


def test_womensrole():
  """Test module womensrole.py by downloading
   womensrole.csv and testing shape of
   extracted data has 42 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = womensrole(test_path)
  try:
    assert x_train.shape == (42, 4)
  except:
    shutil.rmtree(test_path)
    raise()
