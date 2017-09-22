from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.galton2 import galton2


def test_galton2():
  """Test module galton2.py by downloading
   galton2.csv and testing shape of
   extracted data has 898 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = galton2(test_path)
  try:
    assert x_train.shape == (898, 6)
  except:
    shutil.rmtree(test_path)
    raise()
