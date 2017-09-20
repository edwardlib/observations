from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fair import fair


def test_fair():
  """Test module fair.py by downloading
   fair.csv and testing shape of
   extracted data has 601 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fair(test_path)
  try:
    assert x_train.shape == (601, 9)
  except:
    shutil.rmtree(test_path)
    raise()
