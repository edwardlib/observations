from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rivers import rivers


def test_rivers():
  """Test module rivers.py by downloading
   rivers.csv and testing shape of
   extracted data has 141 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rivers(test_path)
  try:
    assert x_train.shape == (141, 1)
  except:
    shutil.rmtree(test_path)
    raise()
