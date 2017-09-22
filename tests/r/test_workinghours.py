from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.workinghours import workinghours


def test_workinghours():
  """Test module workinghours.py by downloading
   workinghours.csv and testing shape of
   extracted data has 3382 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = workinghours(test_path)
  try:
    assert x_train.shape == (3382, 12)
  except:
    shutil.rmtree(test_path)
    raise()
