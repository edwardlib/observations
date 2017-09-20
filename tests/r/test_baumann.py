from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.baumann import baumann


def test_baumann():
  """Test module baumann.py by downloading
   baumann.csv and testing shape of
   extracted data has 66 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = baumann(test_path)
  try:
    assert x_train.shape == (66, 6)
  except:
    shutil.rmtree(test_path)
    raise()
