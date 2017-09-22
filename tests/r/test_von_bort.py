from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.von_bort import von_bort


def test_von_bort():
  """Test module von_bort.py by downloading
   von_bort.csv and testing shape of
   extracted data has 280 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = von_bort(test_path)
  try:
    assert x_train.shape == (280, 4)
  except:
    shutil.rmtree(test_path)
    raise()
