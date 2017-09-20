from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hartnagel import hartnagel


def test_hartnagel():
  """Test module hartnagel.py by downloading
   hartnagel.csv and testing shape of
   extracted data has 38 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hartnagel(test_path)
  try:
    assert x_train.shape == (38, 8)
  except:
    shutil.rmtree(test_path)
    raise()
