from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.muscle import muscle


def test_muscle():
  """Test module muscle.py by downloading
   muscle.csv and testing shape of
   extracted data has 60 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = muscle(test_path)
  try:
    assert x_train.shape == (60, 3)
  except:
    shutil.rmtree(test_path)
    raise()
