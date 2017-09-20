from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.electricity import electricity


def test_electricity():
  """Test module electricity.py by downloading
   electricity.csv and testing shape of
   extracted data has 158 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = electricity(test_path)
  try:
    assert x_train.shape == (158, 8)
  except:
    shutil.rmtree(test_path)
    raise()
