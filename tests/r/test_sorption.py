from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sorption import sorption


def test_sorption():
  """Test module sorption.py by downloading
   sorption.csv and testing shape of
   extracted data has 192 rows and 14 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sorption(test_path)
  try:
    assert x_train.shape == (192, 14)
  except:
    shutil.rmtree(test_path)
    raise()
