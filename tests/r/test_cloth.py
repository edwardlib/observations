from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cloth import cloth


def test_cloth():
  """Test module cloth.py by downloading
   cloth.csv and testing shape of
   extracted data has 32 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cloth(test_path)
  try:
    assert x_train.shape == (32, 2)
  except:
    shutil.rmtree(test_path)
    raise()
