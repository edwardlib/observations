from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bowley import bowley


def test_bowley():
  """Test module bowley.py by downloading
   bowley.csv and testing shape of
   extracted data has 45 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bowley(test_path)
  try:
    assert x_train.shape == (45, 2)
  except:
    shutil.rmtree(test_path)
    raise()
