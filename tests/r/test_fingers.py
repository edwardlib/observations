from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fingers import fingers


def test_fingers():
  """Test module fingers.py by downloading
   fingers.csv and testing shape of
   extracted data has 12 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fingers(test_path)
  try:
    assert x_train.shape == (12, 3)
  except:
    shutil.rmtree(test_path)
    raise()
