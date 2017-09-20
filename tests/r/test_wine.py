from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.wine import wine


def test_wine():
  """Test module wine.py by downloading
   wine.csv and testing shape of
   extracted data has 21 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wine(test_path)
  try:
    assert x_train.shape == (21, 5)
  except:
    shutil.rmtree(test_path)
    raise()
