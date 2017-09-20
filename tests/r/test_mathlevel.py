from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mathlevel import mathlevel


def test_mathlevel():
  """Test module mathlevel.py by downloading
   mathlevel.csv and testing shape of
   extracted data has 609 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mathlevel(test_path)
  try:
    assert x_train.shape == (609, 8)
  except:
    shutil.rmtree(test_path)
    raise()
