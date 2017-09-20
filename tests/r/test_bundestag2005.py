from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bundestag2005 import bundestag2005


def test_bundestag2005():
  """Test module bundestag2005.py by downloading
   bundestag2005.csv and testing shape of
   extracted data has 16 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bundestag2005(test_path)
  try:
    assert x_train.shape == (16, 5)
  except:
    shutil.rmtree(test_path)
    raise()
