from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bod import bod


def test_bod():
  """Test module bod.py by downloading
   bod.csv and testing shape of
   extracted data has 6 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bod(test_path)
  try:
    assert x_train.shape == (6, 2)
  except:
    shutil.rmtree(test_path)
    raise()
