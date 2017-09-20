from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fossum import fossum


def test_fossum():
  """Test module fossum.py by downloading
   fossum.csv and testing shape of
   extracted data has 43 rows and 14 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fossum(test_path)
  try:
    assert x_train.shape == (43, 14)
  except:
    shutil.rmtree(test_path)
    raise()
